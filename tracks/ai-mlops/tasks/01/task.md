# AI-01 · Корпус и детерминированный baseline

Направление: [AI / RAG / MLOps · Python, FastAPI и FAISS](../../README.md). Ориентир: 6–10 часов после изучения темы. Предыдущий шаг: Вводная диагностика и подготовка среды.

## Цель

Подготовить данные и простой поиск для сравнения.

## Входные материалы

[PulseLab](../../../../docs/01-project/pulselab.md), [fixtures](../../../../shared/fixtures/README.md), [контракты](../../../../shared/contracts/README.md). Используй свой код предыдущего задания; внешний backend/аккаунт/оборудование не являются зависимостью.

## Сделать

Прочитай corpus.json и queries.json. Валидируй docId/title/text, создай chunking по абзацам с устойчивыми chunkId и указанием docId. Реализуй простой lexical baseline с документированным tokenization.

Сначала опиши план из 3–5 шагов, затем реализуй минимальный путь и проверь ошибки. Если выбираешь другую библиотеку, объясни совместимость с технологией направления; замена основного стека требует согласования наставника.

## Критерии приёмки

- [ ] Каждый chunk связан с исходным docId и не теряет текст при повторной сборке.
- [ ] Одинаковый corpus/config создаёт одинаковые IDs/fingerprint.
- [ ] Пустой запрос, неизвестное поле и malformed corpus дают понятную ошибку.
- [ ] Baseline возвращает top-k с детерминированной сортировкой; тесты проверяют связи и повторную сборку.

## Сдать в личном публичном GitHub

- Код и осмысленные проверки поведения, ссылка на PR задачи.
- `docs/tasks/01-report.md`: реализация, команды, результаты проверок, решения и ограничения.
- `docs/tasks/01-answers.md`: ответы на [опросник](quiz.md).
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

Пример промпта: «Изучаю AI / RAG / MLOps · Python, FastAPI и FAISS для учебного AI-01. Объясни понятия, необходимые для цели “Подготовить данные и простой поиск для сравнения.”, и дай маленькие отдельные упражнения. Не решай задание целиком. Сверяй API с моей версией и официальной документацией».
