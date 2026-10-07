# Синтетические fixtures

Все данные созданы для PulseLab с нуля. Они не являются записью наблюдений, выгрузкой системы или информацией о реальных людях. Нет имён, контактов, документов и реальных device IDs.

| Файл | Назначение |
| --- | --- |
| `subjects.json` | Два учебных субъекта |
| `readings.json` | 12 валидных Reading: s001 = 8, s002 = 4 |
| `invalid-readings.json` | Невалидные ReadingInput, ожидается 422 |
| `appointments.json` | Две учебные записи для UI |
| `vendor-a.json` | Вымышленный pulse-provider, Unix milliseconds |
| `vendor-b.json` | Вымышленный glucose-provider, mg/dL и RFC3339 |
| `subject-mapping.json` | Явная связь внешнего и учебного ID |
| `webhook-event.json` | Тело учебного webhook, без подписи и секрета |
| `his-rest.json`, `his-soap.xml` | Один набор appointments в двух transports |

Для Vendor A: `measurement_id → externalId`, `person_key → subjectId` через mapping, `pulse → value`, `source=vendor_mock`, `kind=heart_rate`. Для Vendor B: `id → externalId`, `subject → subjectId`, `amount / 18.0182 → value` с округлением до 3 знаков, `source=vendor_mock`, `kind=glucose`, `unit=mmol/L`. Это формула упражнения, не медицинская консультация.

Webhook содержит одну Vendor A запись: ключ импорта Reading берётся из measurement_id, key event dedup — eventId. HMAC вычисляет студент над точными bytes файла/HTTP body по заданию IN-03; ключ в публичных fixtures отсутствует. Для тестов допустим искусственный ключ, явно ограниченный test-only; рабочие ключи не используются.

Повторы/конфликты/429/503 генерируются собственными тестами из этих fixtures. Не добавляй реальные provider payloads. При создании новых fixtures сохраняй явную учебную маркировку и не используй персональные измерения.
