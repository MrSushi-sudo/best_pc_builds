from config.settings import env

# Redis
REDIS_URL = env.str("REDIS_URL", default="redis://127.0.0.1:6379/0")

# Taskiq
TASKIQ_REDIS_URL = env.str("TASKIQ_REDIS_URL", default=REDIS_URL)
TASKIQ_QUEUE_NAME = env.str("TASKIQ_QUEUE_NAME", default="offers")
# Пустое значение отключает периодическую диагностическую задачу.
TASKIQ_HEALTHCHECK_CRON = env.str("TASKIQ_HEALTHCHECK_CRON", default="")
