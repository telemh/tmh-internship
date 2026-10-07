# BE-06 · Качество сервиса и итоговая защита

Направление: [Backend · Bun, TypeScript, Elysia и GraphQL Yoga](../../README.md). Ориентир: 10–16 часов после изучения темы. Предыдущий шаг: BE-05.

## Цель

Сделать воспроизводимый API и доказать устойчивость ключевых операций.

## Входные материалы

[PulseLab](../../../../docs/01-project/pulselab.md), [fixtures](../../../../shared/fixtures/README.md), [контракты](../../../../shared/contracts/README.md). Используй свой код предыдущего задания; внешний backend/аккаунт/оборудование не являются зависимостью.

## Сделать

Добавь CI для типов и тестов, structured logs без payload, requestId и graceful shutdown. Собери коллекцию учебных запросов или curl-примеры. Повтори полный путь на чистом локальном стенде.

Сначала опиши план из 3–5 шагов, затем реализуй минимальный путь и проверь ошибки. Если выбираешь другую библиотеку, объясни совместимость с технологией направления; замена основного стека требует согласования наставника.

## Критерии приёмки

- [ ] Отдельно проходят typecheck и тесты; зафиксированы Bun/пакеты/образы.
- [ ] SIGTERM прекращает новые операции и корректно закрывает соединения.
- [ ] Readiness становится 503 при недоступной обязательной БД; liveness остаётся 200, пока процесс работает.
- [ ] Отчёт содержит конкурентный сценарий, policy matrix, ограничения и команды запуска; наставник может попросить изменить правило фильтрации.

## Сдать в личном публичном GitHub

- Код и осмысленные проверки поведения, ссылка на PR задачи.
- `docs/tasks/06-report.md`: реализация, команды, результаты проверок, решения и ограничения.
- `docs/tasks/06-answers.md`: ответы на [опросник](quiz.md).
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

Пример промпта: «Изучаю Backend · Bun, TypeScript, Elysia и GraphQL Yoga для учебного BE-06. Объясни понятия, необходимые для цели “Сделать воспроизводимый API и доказать устойчивость ключевых операций.”, и дай маленькие отдельные упражнения. Не решай задание целиком. Сверяй API с моей версией и официальной документацией».
