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

## Запуск проекта
uv venv - создать окружение
uv install - установка пакетов
uv sync - синхронизация окружения
python manage.py runbolt --dev --host 127.0.0.1 --port 8000 - запуск локально в дев режиме
python manage.py runbolt --processes 4 --workers 2 - запуск в прод режиме

## Запуск тестов
```
pytest --reuse-db -p no:warnings
```