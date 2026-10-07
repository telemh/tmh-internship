# AI-04 · FastAPI и ответ с источниками

Направление: [AI / RAG / MLOps · Python, FastAPI и FAISS](../../README.md). Ориентир: 8–12 часов после изучения темы. Предыдущий шаг: AI-03.

## Цель

Выдать поиск через API с проверяемым происхождением.

## Входные материалы

[PulseLab](../../../../docs/01-project/pulselab.md), [fixtures](../../../../shared/fixtures/README.md), [контракты](../../../../shared/contracts/README.md). Используй свой код предыдущего задания; внешний backend/аккаунт/оборудование не являются зависимостью.

## Сделать

Создай отдельный учебный POST /search с query и k, затем POST /answer. Search возвращает chunks; answer отдаёт короткую цитату/выжимку и citations из найденных chunks либо статус insufficient_context. Контракт опиши в своём README/OpenAPI; это не внутренний API ТМХ.

Сначала опиши план из 3–5 шагов, затем реализуй минимальный путь и проверь ошибки. Если выбираешь другую библиотеку, объясни совместимость с технологией направления; замена основного стека требует согласования наставника.

## Критерии приёмки

- [ ] k ограничен 1–10; пустой/слишком длинный query отвергается, max length задан явно.
- [ ] Все citations ссылаются на существующие docId/chunkId и соответствуют использованному тексту.
- [ ] Изменённый mock генератора с выдуманной citation отклоняется проверкой.
- [ ] TestClient/эквивалент проверяет search, answer, invalid input и insufficient_context; платный LLM не требуется.

## Сдать в личном публичном GitHub

- Код и осмысленные проверки поведения, ссылка на PR задачи.
- `docs/tasks/04-report.md`: реализация, команды, результаты проверок, решения и ограничения.
- `docs/tasks/04-answers.md`: ответы на [опросник](quiz.md).
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

Пример промпта: «Изучаю AI / RAG / MLOps · Python, FastAPI и FAISS для учебного AI-04. Объясни понятия, необходимые для цели “Выдать поиск через API с проверяемым происхождением.”, и дай маленькие отдельные упражнения. Не решай задание целиком. Сверяй API с моей версией и официальной документацией».
