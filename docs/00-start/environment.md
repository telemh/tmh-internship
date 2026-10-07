# Рабочая среда

Для всех нужны Git, редактор, терминал, GitHub и браузер. Windows подходит; Linux-задачи выполняются в собственной VM или WSL2 с включённым systemd. macOS подходит для большинства направлений. Публикация iOS-приложения, покупка устройств и платные AI-ключи не требуются.

| Маршрут | Подготовить | Проверить |
| --- | --- | --- |
| Mobile | Flutter stable с Dart, Android SDK или Flutter web | `flutter doctor`, `flutter --version`, `dart --version` |
| Backend / интеграции | Bun, TypeScript; MongoDB 8.0 локально начиная с соответствующей задачи | `bun --version`, запуск собственного маленького TS-файла |
| Frontend | Vue 3 scaffold, совместимый runtime/tooling, TypeScript | старт локального dev-server и production build |
| AI / RAG | Python 3.12+ в отдельном окружении, FastAPI, CPU FAISS, embedding-библиотека | `python --version`, тест импорта пакетов |
| DevOps | Своя Linux VM/WSL2, Docker Engine или Docker Desktop, Compose v2 | `docker version`, `docker compose version`, `systemctl --version` |

Конкретные команды установки бери в [официальных источниках](../resources.md). Не запускай неизвестные install-скрипты, предложенные AI, без чтения. Проверь требования SDK к твоей OS.

Для Vue-инструментов Node.js допустим как учебный runtime сборки, если это требуется выбранной версией tooling; это не изменение Bun-backend ТМХ. Для Python сохраняй виртуальную среду вне Git и точные зависимости в manifest/lock-файле.

Все маршруты стартуют с fixtures без backend. БД, cache и S3 добавляются по мере задания. В AI-направлении GPU не требуется; базовый путь использует небольшой multilingual-e5-small на CPU. Сравнение с large — дополнительное исследование при наличии ресурсов.

В README укажи OS, версии, команды установки зависимостей, запуска и тестов. Если требуется VM или WSL, опиши шаги. Читатель должен повторить работу на чистом окружении без обращения к автору за паролями.
