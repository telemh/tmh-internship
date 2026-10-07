# BE-01 · HTTP API в памяти

Направление: [Backend · Bun, TypeScript, Elysia и GraphQL Yoga](../../README.md). Ориентир: 6–8 часов после изучения темы. Предыдущий шаг: Вводная диагностика и подготовка среды.

## Цель

Реализовать строгий вход и понятный контракт ответа.

## Входные материалы

[PulseLab](../../../../docs/01-project/pulselab.md), [fixtures](../../../../shared/fixtures/README.md), [контракты](../../../../shared/contracts/README.md). Используй свой код предыдущего задания; внешний backend/аккаунт/оборудование не являются зависимостью.

## Сделать

Создай Bun/TS-проект с Elysia, health/live, health/ready и GET/POST readings. На этом шаге repository в памяти; начальные данные — shared fixtures. Нормализуй ошибки согласно учебному контракту.

Сначала опиши план из 3–5 шагов, затем реализуй минимальный путь и проверь ошибки. Если выбираешь другую библиотеку, объясни совместимость с технологией направления; замена основного стека требует согласования наставника.

## Критерии приёмки

- [ ] GET фильтрует, сортирует и считает total до limit/offset.
- [ ] POST реализует 201/200/409 для нового ключа, повтора и конфликта.
- [ ] Неверные body/query, неизвестные поля и from > to дают 422 без stack trace.
- [ ] Есть bun test для пагинации, дубля, конфликта и испорченного входа; доступ пока строго локальный.

## Сдать в личном публичном GitHub

- Код и осмысленные проверки поведения, ссылка на PR задачи.
- `docs/tasks/01-report.md`: реализация, команды, результаты проверок, решения и ограничения.
- `docs/tasks/01-answers.md`: ответы на [опросник](quiz.md).
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

Пример промпта: «Изучаю Backend · Bun, TypeScript, Elysia и GraphQL Yoga для учебного BE-01. Объясни понятия, необходимые для цели “Реализовать строгий вход и понятный контракт ответа.”, и дай маленькие отдельные упражнения. Не решай задание целиком. Сверяй API с моей версией и официальной документацией».
