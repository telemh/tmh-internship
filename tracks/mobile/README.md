# Mobile · Dart и Flutter

Dart — типизированный язык с null safety, Future и Stream. Flutter строит интерфейс из widgets и позволяет разделить отображение, состояние и работу с данными. Для ТМХ важны понятные статусы измерений, работа при нестабильной сети и контролируемый доступ к данным устройства.

Не фиксируем внутреннюю библиотеку управления состоянием: для учебного проекта выбери простой подход и объясни его. Эмулятор BLE и health-provider заменяют hardware и системные кабинеты.

## Где эти технологии применяются в ТМХ

1. Flutter показывает пациенту измерения и документы в мобильном приложении. В задании это список синтетических Reading и карточка записи.

2. Источники измерений подключаются через устройства и health-платформы. В задании это Stream эмулятора с отключениями и повторными событиями.

3. Уведомления помогают возвращаться к нужному действию в приложении. В задании это локальная имитация уведомления с переходом в экран; отправка FCM не требуется.

Это общие функциональные примеры. Поля и endpoints упражнений относятся к PulseLab, не раскрывают реализацию продукта.

## Что изучить перед задачами

1. Dart: классы, nullable-типы, JSON, исключения, Future/Stream.
2. Flutter: widget tree, layout, формы, lifecycle и навигация.
3. Разделение UI/state/repository; состояния loading/empty/error/data.
4. Unit/widget-тесты, fake clock и fake repositories.

## Материалы

- [Dart language](https://dart.dev/language)
- [Learn Flutter](https://docs.flutter.dev/learn)
- [Flutter architecture](https://docs.flutter.dev/app-architecture)
- [Flutter testing](https://docs.flutter.dev/testing/overview)
- [Bluetooth technology overview](https://www.bluetooth.com/learn-about-bluetooth/tech-overview/)
- [Health Connect](https://developer.android.com/health-and-fitness/health-connect)
- [HealthKit](https://developer.apple.com/documentation/healthkit)
- [Firebase Cloud Messaging](https://firebase.google.com/docs/cloud-messaging)

Сначала язык и базовая технология, затем соответствующий раздел API/ошибок/тестов. Версии зафиксируй в своём проекте; [статусы источников](../../docs/resources.md). Пример запроса AI: «Я студент с опытом [опыт]. Составь путь изучения тем выше за [часы], опираясь на официальные источники. Для каждой темы дай короткое объяснение и маленькое упражнение, которое не решает мою задачу целиком».

## Практика

Шесть задач по порядку; общий ориентир 46–68 часов плюс изучение незнакомых понятий. Каждая заканчивается публикацией артефактов в своём репозитории и опросником.

| Задача | Часы | После выполнения |
| --- | ---: | --- |
| [MO-01 · Модель измерения и работа с JSON](tasks/01/task.md) | 6–10 | [Опросник](tasks/01/quiz.md) |
| [MO-02 · Журнал и карточка измерения](tasks/02/task.md) | 8–12 | [Опросник](tasks/02/quiz.md) |
| [MO-03 · Сеть, загрузка и повтор запроса](tasks/03/task.md) | 8–12 | [Опросник](tasks/03/quiz.md) |
| [MO-04 · Добавление записи и очередь offline](tasks/04/task.md) | 8–10 | [Опросник](tasks/04/quiz.md) |
| [MO-05 · Эмулятор устройства и разрешений](tasks/05/task.md) | 8–12 | [Опросник](tasks/05/quiz.md) |
| [MO-06 · Завершённое демо и проверка качества](tasks/06/task.md) | 8–12 | [Опросник](tasks/06/quiz.md) |

Начни с [общих правил](../../SECURITY.md) и [инструкции сдачи](../../docs/00-start/submission.md). [Оценивание](../../assessment/rubric.md) открыто заранее. Если нет нужного hardware/OS, обязательный маршрут выполняется через указанные mocks.
