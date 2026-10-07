# AI-02 · Embeddings и FAISS на CPU

Направление: [AI / RAG / MLOps · Python, FastAPI и FAISS](../../README.md). Ориентир: 8–12 часов после изучения темы. Предыдущий шаг: AI-01.

## Цель

Сравнить векторный поиск с простым baseline.

## Входные материалы

[PulseLab](../../../../docs/01-project/pulselab.md), [fixtures](../../../../shared/fixtures/README.md), [контракты](../../../../shared/contracts/README.md). Используй свой код предыдущего задания; внешний backend/аккаунт/оборудование не являются зависимостью.

## Сделать

Построй CPU FAISS IndexFlatIP поверх normalized embeddings multilingual-e5-small. Для асимметричного поиска используй query: и passage: согласно model card; зафиксируй model revision. Свяжи внутренние index positions с chunkId.

Сначала опиши план из 3–5 шагов, затем реализуй минимальный путь и проверь ошибки. Если выбираешь другую библиотеку, объясни совместимость с технологией направления; замена основного стека требует согласования наставника.

## Критерии приёмки

- [ ] Поиск возвращает chunkId/docId/text/score; mapping сохраняется после save/load.
- [ ] Query и passage имеют корректные prefixes; векторы нормализованы.
- [ ] Несовпадение размерности/model revision не загружается молча.
- [ ] Отчёт сравнивает lexical/vector на одинаковых queries; large/HNSW описаны как необязательное расширение.

## Сдать в личном публичном GitHub

- Код и осмысленные проверки поведения, ссылка на PR задачи.
- `docs/tasks/02-report.md`: реализация, команды, результаты проверок, решения и ограничения.
- `docs/tasks/02-answers.md`: ответы на [опросник](quiz.md).
- Обновлённые README, зависимости/lock и AI-журнал; при UI — скриншот/видео на fixtures.

Оформление — по [инструкции сдачи](../../../../docs/00-start/submission.md). Готовые решения здесь не публикуются.

## Как изучать

Не нужно читать все руководства целиком: открой разделы по теме текущей задачи. Полный маршрут изучения указан во [вводной направления](../../README.md).

- [Python tutorial](https://docs.python.org/3/tutorial/)
- [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/)
- [FAISS official repository](https://github.com/facebookresearch/faiss)
- [multilingual-e5-large model card](https://huggingface.co/intfloat/multilingual-e5-large)
- [multilingual-e5-small model card](https://huggingface.co/intfloat/multilingual-e5-small)
- [multilingual-e5-small README](https://huggingface.co/intfloat/multilingual-e5-small/raw/main/README.md)
- [Sentence Transformers usage](https://sbert.net/docs/sentence_transformer/usage/usage.html)
- [pytest](https://docs.pytest.org/en/stable/)
- [Docker Compose](https://docs.docker.com/compose/)

Пример промпта: «Изучаю AI / RAG / MLOps · Python, FastAPI и FAISS для учебного AI-02. Объясни понятия, необходимые для цели “Сравнить векторный поиск с простым baseline.”, и дай маленькие отдельные упражнения. Не решай задание целиком. Сверяй API с моей версией и официальной документацией».
