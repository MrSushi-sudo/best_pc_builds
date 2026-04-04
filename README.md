# Portal Hub
Апи приложения «Лучшие сборки компьютеров»

## Стек
- REST API: **Django Bolt**
- API Documentation: **Swagger**
- Storage: **PostgresSQL**
- Worker: **Celery**
- Message broker: **RabbitMQ**
- Broker Result: **Redis**
- PM: **uv**

## Структура проекта
- `best_pc_builds` - основное приложение
- `users` - пользовательское приложение

## Запуск проекта
- `uv venv` - создать окружение
- `uv install` - установка пакетов
- `uv sync` - синхронизация окружения
- `python manage.py runbolt --dev --host 127.0.0.1 --port 8000` - запуск локально в дев режиме
- `python manage.py runbolt --processes 4 --workers 2` - запуск в прод режиме

## Запуск тестов
```
pytest --reuse-db -p no:warnings
```

## Линт и автоформатирование
- `uv sync --locked --all-groups` - синхронизировать окружение и установить все группы зависимостей, включая dev.
- `uv run pre-commit install` - установить git-хук `pre-commit` для автоматической проверки перед коммитом.
- `uv run pre-commit run --all-files` - запустить все pre-commit проверки на всех файлах проекта.
- `uv run ruff format src` - автоматически отформатировать Python-код в каталоге `src`.
- `uv run ruff check --fix src` - проверить код линтером Ruff и автоматически исправить поддерживаемые проблемы (включая сортировку импортов).
