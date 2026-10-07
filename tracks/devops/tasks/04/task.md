# DO-04 · Backup с доказанным restore

Направление: [DevOps · Linux, systemd, Docker Compose и CI](../../README.md). Ориентир: 8–12 часов после изучения темы. Предыдущий шаг: DO-03.

## Цель

Проверить восстановление, а не только существование файла.

## Входные материалы

[PulseLab](../../../../docs/01-project/pulselab.md), [fixtures](../../../../shared/fixtures/README.md), [контракты](../../../../shared/contracts/README.md). Используй свой код предыдущего задания; внешний backend/аккаунт/оборудование не являются зависимостью.

## Сделать

Создай backup только учебной MongoDB с fixtures и самостоятельно созданными учебными object-файлами. Восстанови в новую пустую БД/каталог, сохрани исходный стенд. Напиши manifest с hash, количеством записей и временем.

Сначала опиши план из 3–5 шагов, затем реализуй минимальный путь и проверь ошибки. Если выбираешь другую библиотеку, объясни совместимость с технологией направления; замена основного стека требует согласования наставника.

## Критерии приёмки

- [ ] Restore не перезаписывает исходную БД и не требует её очистки.
- [ ] После restore совпадают counts, ключи и hashes файлов; один объект можно прочитать.
- [ ] Повреждённый backup обнаруживается проверкой и не даёт ложный PASS.
- [ ] Отчёт определяет учебные RPO/RTO как цель и измеренный результат; реальные backups не используются.

## Сдать в личном публичном GitHub

- Код и осмысленные проверки поведения, ссылка на PR задачи.
- `docs/tasks/04-report.md`: реализация, команды, результаты проверок, решения и ограничения.
- `docs/tasks/04-answers.md`: ответы на [опросник](quiz.md).
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

Пример промпта: «Изучаю DevOps · Linux, systemd, Docker Compose и CI для учебного DO-04. Объясни понятия, необходимые для цели “Проверить восстановление, а не только существование файла.”, и дай маленькие отдельные упражнения. Не решай задание целиком. Сверяй API с моей версией и официальной документацией».
