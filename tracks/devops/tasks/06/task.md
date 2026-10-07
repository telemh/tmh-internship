# DO-06 · CI, release и rollback

Направление: [DevOps · Linux, systemd, Docker Compose и CI](../../README.md). Ориентир: 8–14 часов после изучения темы. Предыдущий шаг: DO-05.

## Цель

Собрать воспроизводимый выпуск и восстановление версии.

## Входные материалы

[PulseLab](../../../../docs/01-project/pulselab.md), [fixtures](../../../../shared/fixtures/README.md), [контракты](../../../../shared/contracts/README.md). Используй свой код предыдущего задания; внешний backend/аккаунт/оборудование не являются зависимостью.

## Сделать

Добавь GitHub Actions с checks/tests без write permissions и секретов. Выпусти локальный immutable release по commit/tag; подготовь rollback приложения без уничтожения данных. Проверяй выпуск в новой учебной VM/чистом окружении.

Сначала опиши план из 3–5 шагов, затем реализуй минимальный путь и проверь ошибки. Если выбираешь другую библиотеку, объясни совместимость с технологией направления; замена основного стека требует согласования наставника.

## Критерии приёмки

- [ ] CI проверяет конфигурации и тесты; PR из fork не запускает привилегированный код с секретами.
- [ ] Release manifest указывает commit, runtime, зависимости и config placeholders.
- [ ] Rollback возвращает прежний app и smoke test, данные сохраняются.
- [ ] README содержит точные start/stop/restore/rollback команды и ограничения; публичный сервер не требуется.

## Сдать в личном публичном GitHub

- Код и осмысленные проверки поведения, ссылка на PR задачи.
- `docs/tasks/06-report.md`: реализация, команды, результаты проверок, решения и ограничения.
- `docs/tasks/06-answers.md`: ответы на [опросник](quiz.md).
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

Пример промпта: «Изучаю DevOps · Linux, systemd, Docker Compose и CI для учебного DO-06. Объясни понятия, необходимые для цели “Собрать воспроизводимый выпуск и восстановление версии.”, и дай маленькие отдельные упражнения. Не решай задание целиком. Сверяй API с моей версией и официальной документацией».
