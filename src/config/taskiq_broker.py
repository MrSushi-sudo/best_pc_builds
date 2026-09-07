from django.conf import settings
from taskiq_redis import RedisStreamBroker

broker = RedisStreamBroker(url=settings.TASKIQ_REDIS_URL, queue_name=settings.TASKIQ_QUEUE_NAME)
