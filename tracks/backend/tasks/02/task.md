# BE-02 · MongoDB и конкурентные записи

Направление: [Backend · Bun, TypeScript, Elysia и GraphQL Yoga](../../README.md). Ориентир: 8–12 часов после изучения темы. Предыдущий шаг: BE-01.

## Цель

Перейти к долговременному хранению без гонки дублей.

## Входные материалы

[PulseLab](../../../../docs/01-project/pulselab.md), [fixtures](../../../../shared/fixtures/README.md), [контракты](../../../../shared/contracts/README.md). Используй свой код предыдущего задания; внешний backend/аккаунт/оборудование не являются зависимостью.

## Сделать

Замени in-memory repository на локальную MongoDB 8.0 с выбранным driver. Создай уникальный составной индекс идемпотентности и индекс чтения по субъекту/времени. Добавь seed отдельной командой без удаления чужих данных.

Сначала опиши план из 3–5 шагов, затем реализуй минимальный путь и проверь ошибки. Если выбираешь другую библиотеку, объясни совместимость с технологией направления; замена основного стека требует согласования наставника.

## Критерии приёмки

- [ ] После перезапуска API записи сохраняются; seed повторяем и относится только к учебной БД.
- [ ] 20 конкурентных одинаковых POST создают ровно одну запись; ответы разрешены 201 и 200.
- [ ] Одинаковый ключ с другим value даёт 409, а не silently overwrite.
- [ ] В отчёте есть explain одного запроса и объяснение индекса; проверены database unavailable и чтение после восстановления.

## Сдать в личном публичном GitHub

- Код и осмысленные проверки поведения, ссылка на PR задачи.
- `docs/tasks/02-report.md`: реализация, команды, результаты проверок, решения и ограничения.
- `docs/tasks/02-answers.md`: ответы на [опросник](quiz.md).
- Обновлённые README, зависимости/lock и AI-журнал; при UI — скриншот/видео на fixtures.

Оформление — по [инструкции сдачи](../../../../docs/00-start/submission.md). Готовые решения здесь не публикуются.

## Как изучать

Не нужно читать все руководства целиком: открой разделы по теме текущей задачи. Полный маршрут изучения указан во [вводной направления](../../README.md).

- [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html)
- [Bun docs](https://bun.com/docs)
- [Elysia Quick Start](https://elysiajs.com/quick-start)
- [Elysia Validation](https://elysiajs.com/essential/validation)
- [GraphQL Learn](https://graphql.org/learn/)
- [Yoga + Bun](https://the-guild.dev/graphql/yoga-server/docs/integrations/integration-with-bun)
- [MongoDB Manual 8.0](https://www.mongodb.com/docs/v8.0/)
- [MongoDB JS driver](https://www.mongodb.com/docs/drivers/node/current/)
- [Valkey topics](https://valkey.io/topics/)
- [Amazon S3 user guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)
- [Bun test](https://bun.com/docs/test)

Пример промпта: «Изучаю Backend · Bun, TypeScript, Elysia и GraphQL Yoga для учебного BE-02. Объясни понятия, необходимые для цели “Перейти к долговременному хранению без гонки дублей.”, и дай маленькие отдельные упражнения. Не решай задание целиком. Сверяй API с моей версией и официальной документацией».
