# Backend · Bun, TypeScript, Elysia и GraphQL Yoga

TypeScript помогает описывать модели и допустимые варианты, но не защищает от неверного JSON без runtime-проверки. Bun запускает JS/TS и предоставляет инструменты работы с пакетами и тестами. Elysia организует HTTP-маршруты и валидацию, GraphQL Yoga — GraphQL-схему и выполнение запросов.

MongoDB хранит документы; Valkey подходит для временных быстрых данных; S3 отделяет файловое содержимое от metadata. Учебный проект стартует в памяти и постепенно добавляет эти границы.

## Где эти технологии применяются в ТМХ

1. Основной backend ТМХ связывает приложение и кабинет с данными через API. В задании Elysia принимает и выдаёт учебные Reading.

2. GraphQL позволяет клиенту запросить нужные поля. В задании Yoga читает тот же repository, что REST, без повторного бизнес-слоя.

3. В продукте документы и структурированные данные решают разные задачи. В задании metadata хранится отдельно, а S3-адаптер пишет только вымышленный текст.

4. Вспомогательные быстрые данные можно отделять от долговременного хранения. В задании Valkey кеширует синтетический список с явной инвалидизацией.

Это общие функциональные примеры. Поля и endpoints упражнений относятся к PulseLab, не раскрывают реализацию продукта.

## Что изучить перед задачами

1. TS: unknown, narrowing, unions, async, исключения.
2. Elysia: маршруты, schema, HTTP status и error mapping.
3. Repository/policy/transport, MongoDB indexes и атомарная уникальность.
4. GraphQL schema/resolver/context; S3 boundary; cache TTL и invalidation.

## Материалы

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

Сначала язык и базовая технология, затем соответствующий раздел API/ошибок/тестов. Версии зафиксируй в своём проекте; [статусы источников](../../docs/resources.md). Пример запроса AI: «Я студент с опытом [опыт]. Составь путь изучения тем выше за [часы], опираясь на официальные источники. Для каждой темы дай короткое объяснение и маленькое упражнение, которое не решает мою задачу целиком».

## Практика

Шесть задач по порядку; общий ориентир 48–74 часов плюс изучение незнакомых понятий. Каждая заканчивается публикацией артефактов в своём репозитории и опросником.

| Задача | Часы | После выполнения |
| --- | ---: | --- |
| [BE-01 · HTTP API в памяти](tasks/01/task.md) | 6–8 | [Опросник](tasks/01/quiz.md) |
| [BE-02 · MongoDB и конкурентные записи](tasks/02/task.md) | 8–12 | [Опросник](tasks/02/quiz.md) |
| [BE-03 · GraphQL поверх общего слоя](tasks/03/task.md) | 8–12 | [Опросник](tasks/03/quiz.md) |
| [BE-04 · Проверка доступа к субъекту](tasks/04/task.md) | 8–12 | [Опросник](tasks/04/quiz.md) |
| [BE-05 · Файлы и cache через адаптеры](tasks/05/task.md) | 8–14 | [Опросник](tasks/05/quiz.md) |
| [BE-06 · Качество сервиса и итоговая защита](tasks/06/task.md) | 10–16 | [Опросник](tasks/06/quiz.md) |

Начни с [общих правил](../../SECURITY.md) и [инструкции сдачи](../../docs/00-start/submission.md). [Оценивание](../../assessment/rubric.md) открыто заранее. Если нет нужного hardware/OS, обязательный маршрут выполняется через указанные mocks.
