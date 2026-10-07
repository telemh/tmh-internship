# DO-03 · systemd для приложения

Направление: [DevOps · Linux, systemd, Docker Compose и CI](../../README.md). Ориентир: 6–10 часов после изучения темы. Предыдущий шаг: DO-02.

## Цель

Запустить приложение управляемым сервисом без root runtime.

## Входные материалы

[PulseLab](../../../../docs/01-project/pulselab.md), [fixtures](../../../../shared/fixtures/README.md), [контракты](../../../../shared/contracts/README.md). Используй свой код предыдущего задания; внешний backend/аккаунт/оборудование не являются зависимостью.

## Сделать

Создай unit для собственного health-service в учебной VM. Runtime приложения — отдельный непривилегированный пользователь; environment-файл хранится локально с ограниченными правами. Добавь Restart и подходящие ограничения filesystem по фактическим нуждам.

Сначала опиши план из 3–5 шагов, затем реализуй минимальный путь и проверь ошибки. Если выбираешь другую библиотеку, объясни совместимость с технологией направления; замена основного стека требует согласования наставника.

## Критерии приёмки

- [ ] Unit проходит systemd-analyze verify; start/status/restart/stop показаны.
- [ ] App не работает от root; читать/писать может только нужные каталоги.
- [ ] Crash приводит к контролируемому restart без бесконечного быстрого цикла.
- [ ] SIGTERM и соединения закрываются корректно; README объясняет выбранные security-настройки и проверку совместимости с runtime.

## Сдать в личном публичном GitHub

- Код и осмысленные проверки поведения, ссылка на PR задачи.
- `docs/tasks/03-report.md`: реализация, команды, результаты проверок, решения и ограничения.
- `docs/tasks/03-answers.md`: ответы на [опросник](quiz.md).
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

Пример промпта: «Изучаю DevOps · Linux, systemd, Docker Compose и CI для учебного DO-03. Объясни понятия, необходимые для цели “Запустить приложение управляемым сервисом без root runtime.”, и дай маленькие отдельные упражнения. Не решай задание целиком. Сверяй API с моей версией и официальной документацией».
