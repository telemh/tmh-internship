# DevOps · Linux, systemd, Docker Compose и CI

Linux запускает процессы и управляет файлами/доступом. systemd управляет жизненным циклом приложения, Docker Compose описывает инфраструктурные сервисы. В типовом контексте ТМХ основной сервис запускается через systemd, а MongoDB и S3-хранилище относятся к инфраструктуре.

Учебная VM независима от компании. Kubernetes, cloud-account и доступ к рабочим серверам не нужны. GitHub Actions выбран для публичного учебного CI, а не как утверждение об internal pipeline.

## Где эти технологии применяются в ТМХ

1. Основной сервис ТМХ работает под управлением systemd. В задании unit запускает собственный маленький health-service.

2. Docker Compose используется для инфраструктуры. В задании он поднимает локальную учебную MongoDB и при необходимости Valkey.

3. Наблюдение за ошибками помогает эксплуатации. В задании logs и health probes показывают сбой зависимости без реальных telemetry keys.

4. Хранилище должно восстанавливаться, а не только создавать backup. В задании restore проверяется на отдельной учебной БД.

Это общие функциональные примеры. Поля и endpoints упражнений относятся к PulseLab, не раскрывают реализацию продукта.

## Что изучить перед задачами

1. Linux: processes, users, права, ports, signals и logs.
2. Compose: services, networks, volumes и healthchecks.
3. systemd unit, restart, shutdown, environment и least privilege.
4. Backup/restore, release/rollback, CI и reproduction.

## Материалы

- [Docker Compose](https://docs.docker.com/compose/)
- [systemd.service manual](https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html)
- [systemd official manual source](https://github.com/systemd/systemd/blob/main/man/systemd.service.xml)
- [MongoDB Manual 8.0](https://www.mongodb.com/docs/v8.0/)
- [Valkey topics](https://valkey.io/topics/)
- [Amazon S3 user guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)
- [GitHub Actions](https://docs.github.com/en/actions)
- [Pro Git, русский](https://git-scm.com/book/ru/v2)

Сначала язык и базовая технология, затем соответствующий раздел API/ошибок/тестов. Версии зафиксируй в своём проекте; [статусы источников](../../docs/resources.md). Пример запроса AI: «Я студент с опытом [опыт]. Составь путь изучения тем выше за [часы], опираясь на официальные источники. Для каждой темы дай короткое объяснение и маленькое упражнение, которое не решает мою задачу целиком».

## Практика

Шесть задач по порядку; общий ориентир 42–66 часов плюс изучение незнакомых понятий. Каждая заканчивается публикацией артефактов в своём репозитории и опросником.

| Задача | Часы | После выполнения |
| --- | ---: | --- |
| [DO-01 · Linux и минимальный health-service](tasks/01/task.md) | 6–8 | [Опросник](tasks/01/quiz.md) |
| [DO-02 · Compose для MongoDB и cache](tasks/02/task.md) | 8–12 | [Опросник](tasks/02/quiz.md) |
| [DO-03 · systemd для приложения](tasks/03/task.md) | 6–10 | [Опросник](tasks/03/quiz.md) |
| [DO-04 · Backup с доказанным restore](tasks/04/task.md) | 8–12 | [Опросник](tasks/04/quiz.md) |
| [DO-05 · Наблюдение и drill отказа](tasks/05/task.md) | 6–10 | [Опросник](tasks/05/quiz.md) |
| [DO-06 · CI, release и rollback](tasks/06/task.md) | 8–14 | [Опросник](tasks/06/quiz.md) |

Начни с [общих правил](../../SECURITY.md) и [инструкции сдачи](../../docs/00-start/submission.md). [Оценивание](../../assessment/rubric.md) открыто заранее. Если нет нужного hardware/OS, обязательный маршрут выполняется через указанные mocks.
