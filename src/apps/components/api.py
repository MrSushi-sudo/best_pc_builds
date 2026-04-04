from typing import List

from django_bolt import ModelViewSet

from apps.best_pc_builds.api import api
from apps.components.models import Processor
from apps.components.schemas import ProcessorSerializer


@api.viewset("/processor")
class ProcessorViewSet(ModelViewSet):
    """Вьювсет для процессоров"""

    # Отключение доп.эндпоинтов
    create = None
    update = None
    partial_update = None
    destroy = None

    queryset = Processor.objects.all()
    serializer_class = ProcessorSerializer

    async def list(self, request) -> List[ProcessorSerializer]:
        """Список процессоров.
        Возвращает список процессоров.
        """
        return await super().list(request)

    async def retrieve(self, request, **kwargs) -> ProcessorSerializer:
        """Возвращает процессор по id.
        Детальная информация о процессоре.
        """
        return await super().retrieve(request, **kwargs)
