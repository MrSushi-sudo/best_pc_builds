import logging

from config.components.services import TASKIQ_HEALTHCHECK_CRON, TASKIQ_QUEUE_NAME
from config.taskiq_broker import broker

logger = logging.getLogger(__name__)


@broker.task(schedule=[{"cron": TASKIQ_HEALTHCHECK_CRON}])
async def check_queue() -> None:
    """Проверка доставки задачи без обращения к маркетплейсам и базе данных."""
    logger.info("Taskiq: диагностическая задача выполнена (очередь %s)", TASKIQ_QUEUE_NAME)
