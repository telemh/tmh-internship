# DO-01 · Linux и минимальный health-service

Направление: [DevOps · Linux, systemd, Docker Compose и CI](../../README.md). Ориентир: 6–8 часов после изучения темы. Предыдущий шаг: Вводная диагностика и подготовка среды.

## Цель

Понять процесс, порт и жизненный цикл.

## Входные материалы

[PulseLab](../../../../docs/01-project/pulselab.md), [fixtures](../../../../shared/fixtures/README.md), [контракты](../../../../shared/contracts/README.md). Используй свой код предыдущего задания; внешний backend/аккаунт/оборудование не являются зависимостью.

## Сделать

В собственной Linux VM/WSL2 создай маленький Bun/Elysia health-service или свой учебный FastAPI-service. Добавь live/ready и graceful shutdown. Подготовь команды для PID, listening port и logs; источники ТМХ не используются.

Сначала опиши план из 3–5 шагов, затем реализуй минимальный путь и проверь ошибки. Если выбираешь другую библиотеку, объясни совместимость с технологией направления; замена основного стека требует согласования наставника.

## Критерии приёмки

- [ ] Сервис слушает только loopback; в README названы выбранный port и runtime.
- [ ] Live 200; ready 503 при fake dependency failure.
- [ ] SIGTERM приводит к контролируемому завершению без незавершённой записи.
- [ ] Отчёт содержит безопасные локальные команды проверки и разницу process/service/container.

## Сдать в личном публичном GitHub

- Код и осмысленные проверки поведения, ссылка на PR задачи.
- `docs/tasks/01-report.md`: реализация, команды, результаты проверок, решения и ограничения.
- `docs/tasks/01-answers.md`: ответы на [опросник](quiz.md).
- Обновлённые README, зависимости/lock и AI-журнал; при UI — скриншот/видео на fixtures.

Оформление — по [инструкции сдачи](../../../../docs/00-start/submission.md). Готовые решения здесь не публикуются.

## Как изучать

Не нужно читать все руководства целиком: открой разделы по теме текущей задачи. Полный маршрут изучения указан во [вводной направления](../../README.md).

- [Docker Compose](https://docs.docker.com/compose/)
- [systemd.service manual](https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html)
- [systemd official manual source](https://github.com/systemd/systemd/blob/main/man/systemd.service.xml)
- [MongoDB Manual 8.0](https://www.mongodb.com/docs/v8.0/)
- [Valkey topics](https://valkey.io/topics/)
- [Amazon S3 user guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)
- [GitHub Actions](https://docs.github.com/en/actions)
- [Pro Git, русский](https://git-scm.com/book/ru/v2)

Пример промпта: «Изучаю DevOps · Linux, systemd, Docker Compose и CI для учебного DO-01. Объясни понятия, необходимые для цели “Понять процесс, порт и жизненный цикл.”, и дай маленькие отдельные упражнения. Не решай задание целиком. Сверяй API с моей версией и официальной документацией».
