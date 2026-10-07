#!/usr/bin/env python3
"""Offline integrity checks for this curriculum; not a complete security audit."""
import json
import math
import re
import sys
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors = []

def fail(message):
    errors.append(message)

def read_json(rel):
    return json.loads((ROOT / rel).read_text(encoding='utf-8'), parse_constant=lambda x: (_ for _ in ()).throw(ValueError('non-JSON number')))

def check_schema(value, schema):
    # Implements only the explicit subset used by bundled Reading schemas.
    # Applications must use a real JSON Schema validator with date-time enabled.
    st = schema.get('type')
    if st == 'object':
        if not isinstance(value, dict): return False
        if not set(schema.get('required', [])).issubset(value): return False
        props = schema.get('properties', {})
        if schema.get('additionalProperties') is False and set(value) - set(props): return False
        if any(not check_schema(v, props[k]) for k,v in value.items() if k in props): return False
    elif st == 'string':
        if not isinstance(value, str): return False
        if len(value) < schema.get('minLength', 0) or len(value) > schema.get('maxLength', math.inf): return False
        if 'pattern' in schema and not re.search(schema['pattern'],value): return False
        if schema.get('format') == 'date-time':
            try:
                parsed = datetime.fromisoformat(value.replace('Z','+00:00'))
                if parsed.tzinfo is None: return False
            except ValueError: return False
    elif st == 'number':
        if isinstance(value,bool) or not isinstance(value,(int,float)) or not math.isfinite(value): return False
        if value < schema.get('minimum',-math.inf): return False
    if 'enum' in schema and value not in schema['enum']: return False
    if 'const' in schema and value != schema['const']: return False
    if 'oneOf' in schema:
        # Variants constrain object properties without repeating type:object.
        matches=0
        for variant in schema['oneOf']:
            if all(k in value and check_schema(value[k],vs) for k,vs in variant.get('properties',{}).items()): matches+=1
        if matches != 1: return False
    return True

for p in sorted(ROOT.rglob('*')):
    if not p.is_file() or '.git' in p.parts: continue
    rel=p.relative_to(ROOT).as_posix()
    if p.suffix=='.json':
        try: read_json(rel)
        except Exception: fail(f'Invalid JSON: {rel}')
    if p.suffix=='.md':
        body=p.read_text(encoding='utf-8')
        if body.count('```') % 2: fail(f'Unbalanced code fences: {rel}')
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',body):
            if re.match(r'^[a-zA-Z][\w+.-]*:',target) or target.startswith('#'): continue
            dest=target.split('#',1)[0]
            if dest and not (p.parent/dest).exists(): fail(f'Broken relative link: {rel} -> {dest}')
    if p.name == '.env' or p.suffix in ('.pem','.key','.p12','.pfx'):
        fail(f'Unexpected credential file: {rel}')
    # Deliberately narrow heuristics, not a claim of full secret detection.
    if p.suffix in ('.md','.json','.yml','.xml','.txt'):
        body=p.read_text(encoding='utf-8')
        if re.search(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',body): fail(f'Private key marker: {rel}')
        if re.search(r'https?://[^\s/@:]+:[^\s/@]+@',body): fail(f'URL with credentials: {rel}')
        if re.search(r'(?:https?://)?[\w.-]+\.(?:telemedhub\.(?:io|ru)|tail[0-9a-z]+\.ts\.net)',body,re.I):
            fail(f'Unexpected company/infrastructure URL: {rel}')

try:
    catalog=read_json('shared/task-catalog.json')
    if len(catalog)!=36 or len({t['id'] for t in catalog})!=36: fail('Expected 36 unique tasks')
    expected={'mobile':'MO','backend':'BE','frontend':'FE','integrations':'IN','ai-mlops':'AI','devops':'DO'}
    for key,prefix in expected.items():
        tasks=[t for t in catalog if t['track']==key]
        if sorted(t['number'] for t in tasks)!=list(range(1,7)): fail(f'Task numbers: {key}')
        for t in tasks:
            if t['id']!=f"{prefix}-{t['number']:02d}": fail(f"Invalid task id: {t['id']}")
            for field in ('task','quiz'):
                if not (ROOT/t[field]).is_file(): fail(f"Missing {field}: {t['id']}")
            task=(ROOT/t['task']).read_text(encoding='utf-8')
            if task.count('- [ ]')<4: fail(f"Insufficient acceptance criteria: {t['id']}")
            quiz=(ROOT/t['quiz']).read_text(encoding='utf-8')
            if '4.' not in quiz or '<details>' not in quiz: fail(f"Incomplete quiz: {t['id']}")
            expected_dep=[] if t['number']==1 else [f"{prefix}-{t['number']-1:02d}"]
            if t['dependsOn']!=expected_dep: fail(f"Dependency mismatch: {t['id']}")

    rs=read_json('shared/contracts/reading.schema.json')
    ins=read_json('shared/contracts/reading-input.schema.json')
    readings=read_json('shared/fixtures/readings.json')
    subjects=read_json('shared/fixtures/subjects.json')
    if len(readings)!=12 or sum(r['subjectId']=='s001' for r in readings)!=8: fail('Fixture counts mismatch')
    if len({r['id'] for r in readings})!=len(readings): fail('Duplicate reading ids')
    if len({(r['subjectId'],r['source'],r['externalId']) for r in readings})!=len(readings): fail('Duplicate fixture natural key')
    for r in readings:
        if not check_schema(r,rs): fail('Valid reading rejected by schema subset')
        if r['subjectId'] not in {s['id'] for s in subjects}: fail('Unknown fixture subject')
        if not check_schema({k:v for k,v in r.items() if k!='id'},ins): fail('Valid input rejected')
    for bad in read_json('shared/fixtures/invalid-readings.json'):
        if check_schema(bad['payload'],ins): fail(f"Invalid fixture accepted: {bad['caseId']}")
    api=read_json('shared/contracts/openapi.json')
    if api['openapi']!='3.1.0': fail('Unexpected OpenAPI version')
    for name,sch in [('Reading',rs),('ReadingInput',ins)]:
        if api['components']['schemas'][name]!={k:v for k,v in sch.items() if k!='$schema'}: fail(f'OpenAPI schema mismatch: {name}')
    def walk_refs(value):
        if isinstance(value,dict):
            if '$ref' in value:
                ref=value['$ref']
                if ref.startswith('#/'):
                    current=api
                    try:
                        for part in ref[2:].split('/'): current=current[part.replace('~1','/').replace('~0','~')]
                    except (KeyError,TypeError): fail(f'Broken OpenAPI ref: {ref}')
            for v in value.values(): walk_refs(v)
        elif isinstance(value,list):
            for v in value: walk_refs(v)
    walk_refs(api)
    soap=ET.parse(ROOT/'shared/fixtures/his-soap.xml').getroot()
    ns={'lab':'urn:pulselab:his:1'}
    mapped=[]
    for a in soap.findall('.//lab:Appointment',ns):
        mapped.append({out:a.find(f'lab:{tag}',ns).text for out,tag in [('id','Id'),('subjectId','SubjectId'),('startsAt','StartsAt'),('status','Status')]})
    if mapped!=read_json('shared/fixtures/his-rest.json')['appointments']: fail('SOAP/REST fixture mismatch')
    docs=read_json('shared/knowledge/corpus.json'); queries=read_json('shared/knowledge/queries.json')
    doc_ids={d['docId'] for d in docs}
    if len(doc_ids)!=len(docs): fail('Duplicate knowledge doc ids')
    if len({q['queryId'] for q in queries})!=len(queries): fail('Duplicate query ids')
    for q in queries:
        if not set(q['relevantDocIds']).issubset(doc_ids): fail(f"Unknown gold doc: {q['queryId']}")
        if q['answerable']!=bool(q['relevantDocIds']): fail(f"Invalid answerability: {q['queryId']}")
        if q['split'] not in ('dev','test'): fail('Invalid query split')
except Exception as e:
    fail(f'Check failed: {type(e).__name__}: {e}')

if errors:
    for e in errors: print('FAIL:',e)
    sys.exit(1)
print('PASS: 36 tasks / 36 quizzes; relative links; JSON; Reading fixtures; OpenAPI refs/schema parity; SOAP/REST; knowledge labels; narrow public-content checks.')
print('External links, SDK installs and student implementations are not tested by this offline check.')
