# DO-05 · Наблюдение и drill отказа

Направление: [DevOps · Linux, systemd, Docker Compose и CI](../../README.md). Ориентир: 6–10 часов после изучения темы. Предыдущий шаг: DO-04.

## Цель

Связать ошибку, health и диагностический результат.

## Входные материалы

[PulseLab](../../../../docs/01-project/pulselab.md), [fixtures](../../../../shared/fixtures/README.md), [контракты](../../../../shared/contracts/README.md). Используй свой код предыдущего задания; внешний backend/аккаунт/оборудование не являются зависимостью.

## Сделать

Добавь JSON logs с requestId/status/duration и локальный сбор метрик count/error/latency. Проведи три drill: БД недоступна, заполнен только учебный ограниченный каталог, app crash. Реальную файловую систему хоста не заполняй.

Сначала опиши план из 3–5 шагов, затем реализуй минимальный путь и проверь ошибки. Если выбираешь другую библиотеку, объясни совместимость с технологией направления; замена основного стека требует согласования наставника.

## Критерии приёмки

- [ ] Нет body, credentials и полных medical payload в logs.
- [ ] Для каждого drill записано ожидание, наблюдение, восстановление и проверка результата.
- [ ] Readiness и liveness ведут себя согласно смыслу; нет ложного success после write failure.
- [ ] Тест заполнения использует quota/mock/малый изолированный ресурс; logs артефакта синтетические.

## Сдать в личном публичном GitHub

- Код и осмысленные проверки поведения, ссылка на PR задачи.
- `docs/tasks/05-report.md`: реализация, команды, результаты проверок, решения и ограничения.
- `docs/tasks/05-answers.md`: ответы на [опросник](quiz.md).
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

Пример промпта: «Изучаю DevOps · Linux, systemd, Docker Compose и CI для учебного DO-05. Объясни понятия, необходимые для цели “Связать ошибку, health и диагностический результат.”, и дай маленькие отдельные упражнения. Не решай задание целиком. Сверяй API с моей версией и официальной документацией».
