# AI-03 · Benchmark без подгонки под тест

Направление: [AI / RAG / MLOps · Python, FastAPI и FAISS](../../README.md). Ориентир: 10–14 часов после изучения темы. Предыдущий шаг: AI-02.

## Цель

Измерять качество поиска и честно описывать ограничения.

## Входные материалы

[PulseLab](../../../../docs/01-project/pulselab.md), [fixtures](../../../../shared/fixtures/README.md), [контракты](../../../../shared/contracts/README.md). Используй свой код предыдущего задания; внешний backend/аккаунт/оборудование не являются зависимостью.

## Сделать

Раздели provided split=dev и split=test; настрой chunking/k на dev. На test посчитай Recall@1/3 и MRR@3 для answerable-запросов. Для unanswerable оцени abstention отдельно, выбирая правило/порог только на dev. Добавь минимум шесть новых synthetic test-запросов с объяснением gold labels.

Сначала опиши план из 3–5 шагов, затем реализуй минимальный путь и проверь ошибки. Если выбираешь другую библиотеку, объясни совместимость с технологией направления; замена основного стека требует согласования наставника.

## Критерии приёмки

- [ ] Формулы и числитель/знаменатель метрик записаны; сравнение baseline и vector на одном наборе.
- [ ] Test не используется для выбора threshold, chunk size и k.
- [ ] Отчёт отдельно показывает answerable/unanswerable; similarity не объявляется вероятностью корректного ответа.
- [ ] Сохраняются результаты по каждому queryId, ограничения малого набора и время CPU-инференса; обещания production-точности отсутствуют.

## Сдать в личном публичном GitHub

- Код и осмысленные проверки поведения, ссылка на PR задачи.
- `docs/tasks/03-report.md`: реализация, команды, результаты проверок, решения и ограничения.
- `docs/tasks/03-answers.md`: ответы на [опросник](quiz.md).
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

Пример промпта: «Изучаю AI / RAG / MLOps · Python, FastAPI и FAISS для учебного AI-03. Объясни понятия, необходимые для цели “Измерять качество поиска и честно описывать ограничения.”, и дай маленькие отдельные упражнения. Не решай задание целиком. Сверяй API с моей версией и официальной документацией».
