# AI / RAG / MLOps · Python, FastAPI и FAISS

RAG ищет релевантные фрагменты и строит ответ с опорой на них. Python удобен для обработки текстов и экспериментов, FastAPI — для HTTP-сервиса, FAISS — для поиска ближайших векторов. В отдельных AI-компонентах ТМХ применяется multilingual-e5; основная продуктовая логика остаётся в своём backend.

Здесь поиск только по справке PulseLab: никаких медицинских рекомендаций, постановки диагноза и реальных клинических документов. Для обязательных задач достаточно CPU и multilingual-e5-small. LLM/платные ключи не нужны: ответ extractive или детерминированный mock.

## Где эти технологии применяются в ТМХ

1. В AI-сервисах ТМХ embeddings/FAISS используются для поиска контекста. В задании они ищут разделы авторской справки PulseLab.

2. API делает AI-компонент доступным другим частям решения. В задании FastAPI выдаёт поиск и проверяемые citations.

3. Обновление набора документов требует согласованного индекса. В задании manifest связывает corpus, модель и артефакт индекса; broken update сохраняет предыдущую версию.

Это общие функциональные примеры. Поля и endpoints упражнений относятся к PulseLab, не раскрывают реализацию продукта.

## Что изучить перед задачами

1. Python: коллекции, файлы, exceptions, typing и окружения.
2. Corpus/chunk IDs, provenance и fingerprint.
3. Embedding retrieval: query/passage prefixes, normalized vectors, cosine/IP.
4. Recall@k и MRR, abstention и оценка ссылок; atomic release индекса.

## Материалы

- [Python tutorial](https://docs.python.org/3/tutorial/)
- [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/)
- [FAISS official repository](https://github.com/facebookresearch/faiss)
- [multilingual-e5-large model card](https://huggingface.co/intfloat/multilingual-e5-large)
- [multilingual-e5-small model card](https://huggingface.co/intfloat/multilingual-e5-small)
- [multilingual-e5-small README](https://huggingface.co/intfloat/multilingual-e5-small/raw/main/README.md)
- [Sentence Transformers usage](https://sbert.net/docs/sentence_transformer/usage/usage.html)
- [pytest](https://docs.pytest.org/en/stable/)
- [Docker Compose](https://docs.docker.com/compose/)

Сначала язык и базовая технология, затем соответствующий раздел API/ошибок/тестов. Версии зафиксируй в своём проекте; [статусы источников](../../docs/resources.md). Пример запроса AI: «Я студент с опытом [опыт]. Составь путь изучения тем выше за [часы], опираясь на официальные источники. Для каждой темы дай короткое объяснение и маленькое упражнение, которое не решает мою задачу целиком».

## Практика

Шесть задач по порядку; общий ориентир 48–74 часов плюс изучение незнакомых понятий. Каждая заканчивается публикацией артефактов в своём репозитории и опросником.

| Задача | Часы | После выполнения |
| --- | ---: | --- |
| [AI-01 · Корпус и детерминированный baseline](tasks/01/task.md) | 6–10 | [Опросник](tasks/01/quiz.md) |
| [AI-02 · Embeddings и FAISS на CPU](tasks/02/task.md) | 8–12 | [Опросник](tasks/02/quiz.md) |
| [AI-03 · Benchmark без подгонки под тест](tasks/03/task.md) | 10–14 | [Опросник](tasks/03/quiz.md) |
| [AI-04 · FastAPI и ответ с источниками](tasks/04/task.md) | 8–12 | [Опросник](tasks/04/quiz.md) |
| [AI-05 · Версия индекса и атомарное обновление](tasks/05/task.md) | 8–12 | [Опросник](tasks/05/quiz.md) |
| [AI-06 · RAG-границы, CI и финальная демонстрация](tasks/06/task.md) | 8–14 | [Опросник](tasks/06/quiz.md) |

Начни с [общих правил](../../SECURITY.md) и [инструкции сдачи](../../docs/00-start/submission.md). [Оценивание](../../assessment/rubric.md) открыто заранее. Если нет нужного hardware/OS, обязательный маршрут выполняется через указанные mocks.
