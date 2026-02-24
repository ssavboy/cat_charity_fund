# QRKot — фонд помощи котикам

Проект QRKot — это бекенд‑приложение для благотворительного фонда поддержки котиков. Сервис позволяет собирать пожертвования и распределять их по благотворительным проектам фонда.

## Основные возможности

- Создание благотворительных проектов с целевой суммой и описанием.
- Создание пожертвований пользователями фонда.
- Автоматическое распределение пожертвований по открытым проектам по принципу «первый открылся — первым финансируется».
- Асинхронный API на FastAPI с валидацией входных данных и схемами Pydantic.
- Документация API в формате Swagger и ReDoc.

## Технологии

- Python 3.9.
- FastAPI.
- SQLAlchemy (async).
- Asyncio.
- SQLite (по умолчанию).
- Alembic для миграций.

## Установка и запуск

Клонируйте репозиторий и перейдите в директорию проекта:

```bash
git clone git@github.com:ssavboy/cat_charity_fund.git
cd cat_charity_fund
```

Создайте и активируйте виртуальное окружение:

```bash
python3 -m venv venv

# Linux / macOS
source venv/bin/activate

# Windows
source venv/scripts/activate
```

Обновите pip и установите зависимости:

```bash
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

Примените миграции базы данных:

```bash
alembic upgrade head
```

Запустите приложение:

```bash
uvicorn app.main:app
```

После запуска документация будет доступна по адресам:

- Swagger: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Структура проекта

```text
cat_charity_fund/
├── app/
│   ├── api/        # маршруты и роутеры FastAPI
│   ├── core/       # настройки приложения (конфиг, зависимости)
│   ├── crud/       # слой работы с БД (CRUD-операции)
│   ├── models/     # модели SQLAlchemy
│   ├── schemas/    # Pydantic-схемы
│   ├── sevices/    # бизнес-логика, в т.ч. интеграции (Google Sheets и др.)
│   ├── __init__.py
│   └── main.py     # точка входа FastAPI-приложения
├── alembic/        # миграции БД
├── tests/          # тесты
├── alembic.ini
├── fastapi.db      # SQLite-база (dev)
├── openapi.json    # сгенерированная спецификация API
├── pytest.ini
├── requirements.txt
├── .flake8
├── .gitignore
└── README.md
```
