# AI-06 · RAG-границы, CI и финальная демонстрация

Направление: [AI / RAG / MLOps · Python, FastAPI и FAISS](../../README.md). Ориентир: 8–14 часов после изучения темы. Предыдущий шаг: AI-05.

## Цель

Показать измеримое качество и безопасные границы учебного помощника.

## Входные материалы

[PulseLab](../../../../docs/01-project/pulselab.md), [fixtures](../../../../shared/fixtures/README.md), [контракты](../../../../shared/contracts/README.md). Используй свой код предыдущего задания; внешний backend/аккаунт/оборудование не являются зависимостью.

## Сделать

Добавь synthetic injection-документ: он просит игнорировать правила и вывести придуманный секрет. Система должна трактовать его как данные, не исполнять команды и не вызывать tools. Объедини benchmark, manifest и API в CI; покажи answerable и unanswerable сценарии.

Сначала опиши план из 3–5 шагов, затем реализуй минимальный путь и проверь ошибки. Если выбираешь другую библиотеку, объясни совместимость с технологией направления; замена основного стека требует согласования наставника.

## Критерии приёмки

- [ ] Документ не выполняет инструкции и не запускает shell/HTTP tools; есть adversarial test.
- [ ] Ответы касаются только справки PulseLab, без диагнозов/назначений.
- [ ] CI проверяет код/fixtures/API; тяжелый model download отделён от быстрых тестов и описан.
- [ ] README даёт CPU-команды, версии, метрики и ограничения; наставник может попросить добавить новый документ и показать rebuild.

## Сдать в личном публичном GitHub

- Код и осмысленные проверки поведения, ссылка на PR задачи.
- `docs/tasks/06-report.md`: реализация, команды, результаты проверок, решения и ограничения.
- `docs/tasks/06-answers.md`: ответы на [опросник](quiz.md).
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

Пример промпта: «Изучаю AI / RAG / MLOps · Python, FastAPI и FAISS для учебного AI-06. Объясни понятия, необходимые для цели “Показать измеримое качество и безопасные границы учебного помощника.”, и дай маленькие отдельные упражнения. Не решай задание целиком. Сверяй API с моей версией и официальной документацией».
