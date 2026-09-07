import os

import django
from taskiq import TaskiqScheduler
from taskiq.schedule_sources import LabelScheduleSource

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from config.taskiq_broker import broker  # noqa: E402

scheduler = TaskiqScheduler(broker=broker, sources=[LabelScheduleSource(broker)])
