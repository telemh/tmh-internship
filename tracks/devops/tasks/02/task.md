# DO-02 · Compose для MongoDB и cache

Направление: [DevOps · Linux, systemd, Docker Compose и CI](../../README.md). Ориентир: 8–12 часов после изучения темы. Предыдущий шаг: DO-01.

## Цель

Поднять изолированные зависимости с сохранением данных.

## Входные материалы

[PulseLab](../../../../docs/01-project/pulselab.md), [fixtures](../../../../shared/fixtures/README.md), [контракты](../../../../shared/contracts/README.md). Используй свой код предыдущего задания; внешний backend/аккаунт/оборудование не являются зависимостью.

## Сделать

Добавь Compose v2 для MongoDB 8.0 и Valkey, отдельные volumes и healthchecks. Версии образов конкретные. App пока запускается вне Compose; ему передаётся локальная учебная конфигурация. S3 mock остаётся частью приложения.

Сначала опиши план из 3–5 шагов, затем реализуй минимальный путь и проверь ошибки. Если выбираешь другую библиотеку, объясни совместимость с технологией направления; замена основного стека требует согласования наставника.

## Критерии приёмки

- [ ] Опубликованные ports привязаны к 127.0.0.1; БД имеет локально созданные credentials, не в Git.
- [ ] После restart данные сохраняются; down не объявляется backup и инструкции не удаляют volumes по умолчанию.
- [ ] Compose config проходит, dependencies health виден; app ready реагирует на БД.
- [ ] Чистый запуск документирован, отсутствуют latest tags и hardcoded secrets.

## Сдать в личном публичном GitHub

- Код и осмысленные проверки поведения, ссылка на PR задачи.
- `docs/tasks/02-report.md`: реализация, команды, результаты проверок, решения и ограничения.
- `docs/tasks/02-answers.md`: ответы на [опросник](quiz.md).
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

Пример промпта: «Изучаю DevOps · Linux, systemd, Docker Compose и CI для учебного DO-02. Объясни понятия, необходимые для цели “Поднять изолированные зависимости с сохранением данных.”, и дай маленькие отдельные упражнения. Не решай задание целиком. Сверяй API с моей версией и официальной документацией».
