from typing import List

from django_bolt import ModelViewSet, Request

from apps.best_pc_builds.api import api
from apps.components.models import (
    ComputerCase,
    CoolingSystem,
    Motherboard,
    PowerSupply,
    Processor,
    Ram,
    Storage,
    VideoCard,
)
from apps.components.schemas import (
    ComputerCaseSerializer,
    CoolingSystemSerializer,
    MotherboardSerializer,
    PowerSupplySerializer,
    ProcessorSerializer,
    RamSerializer,
    StorageSerializer,
    VideoCardSerializer,
)


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

    async def list(self, request: Request) -> List[ProcessorSerializer]:
        """Список процессоров. Возвращает список процессоров."""
        return await super().list(request)

    async def retrieve(self, request: Request) -> ProcessorSerializer:
        """Возвращает процессор по id. Детальная информация о процессоре."""
        return await super().retrieve(request)


@api.viewset("/motherboard")
class MotherboardViewSet(ModelViewSet):
    """Вьювсет для материнских плат"""

    create = None
    update = None
    partial_update = None
    destroy = None

    queryset = Motherboard.objects.all()
    serializer_class = MotherboardSerializer

    async def list(self, request: Request) -> List[MotherboardSerializer]:
        """Список материнских плат. Возвращает список материнских плат."""
        return await super().list(request)

    async def retrieve(self, request: Request) -> MotherboardSerializer:
        """Возвращает материнскую плату по id. Детальная информация о материнской плате."""
        return await super().retrieve(request)


@api.viewset("/video-card")
class VideoCardViewSet(ModelViewSet):
    """Вьювсет для видеокарт"""

    create = None
    update = None
    partial_update = None
    destroy = None

    queryset = VideoCard.objects.all()
    serializer_class = VideoCardSerializer

    async def list(self, request: Request) -> List[VideoCardSerializer]:
        """Список видеокарт. Возвращает список видеокарт."""
        return await super().list(request)

    async def retrieve(self, request: Request) -> VideoCardSerializer:
        """Возвращает видеокарту по id. Детальная информация о видеокарте."""
        return await super().retrieve(request)


@api.viewset("/ram")
class RamViewSet(ModelViewSet):
    """Вьювсет для оперативной памяти"""

    create = None
    update = None
    partial_update = None
    destroy = None

    queryset = Ram.objects.all()
    serializer_class = RamSerializer

    async def list(self, request: Request) -> List[RamSerializer]:
        """Список оперативной памяти. Возвращает список оперативной памяти."""
        return await super().list(request)

    async def retrieve(self, request: Request) -> RamSerializer:
        """Возвращает оперативную память по id. Детальная информация об оперативной памяти."""
        return await super().retrieve(request)


@api.viewset("/storage")
class StorageViewSet(ModelViewSet):
    """Вьювсет для накопителей"""

    create = None
    update = None
    partial_update = None
    destroy = None

    queryset = Storage.objects.all()
    serializer_class = StorageSerializer

    async def list(self, request: Request) -> List[StorageSerializer]:
        """Список накопителей. Возвращает список накопителей."""
        return await super().list(request)

    async def retrieve(self, request: Request) -> StorageSerializer:
        """Возвращает накопитель по id. Детальная информация о накопителе."""
        return await super().retrieve(request)


@api.viewset("/power-supply")
class PowerSupplyViewSet(ModelViewSet):
    """Вьювсет для блоков питания"""

    create = None
    update = None
    partial_update = None
    destroy = None

    queryset = PowerSupply.objects.all()
    serializer_class = PowerSupplySerializer

    async def list(self, request: Request) -> List[PowerSupplySerializer]:
        """Список блоков питания. Возвращает список блоков питания."""
        return await super().list(request)

    async def retrieve(self, request: Request) -> PowerSupplySerializer:
        """Возвращает блок питания по id. Детальная информация о блоке питания."""
        return await super().retrieve(request)


@api.viewset("/computer-case")
class ComputerCaseViewSet(ModelViewSet):
    """Вьювсет для корпусов"""

    create = None
    update = None
    partial_update = None
    destroy = None

    queryset = ComputerCase.objects.all()
    serializer_class = ComputerCaseSerializer

    async def list(self, request: Request) -> List[ComputerCaseSerializer]:
        """Список корпусов. Возвращает список корпусов."""
        return await super().list(request)

    async def retrieve(self, request: Request) -> ComputerCaseSerializer:
        """Возвращает корпус по id. Детальная информация о корпусе."""
        return await super().retrieve(request)


@api.viewset("/cooling-system")
class CoolingSystemViewSet(ModelViewSet):
    """Вьювсет для систем охлаждения"""

    create = None
    update = None
    partial_update = None
    destroy = None

    queryset = CoolingSystem.objects.all()
    serializer_class = CoolingSystemSerializer

    async def list(self, request: Request) -> List[CoolingSystemSerializer]:
        """Список систем охлаждения. Возвращает список систем охлаждения."""
        return await super().list(request)

    async def retrieve(self, request: Request) -> CoolingSystemSerializer:
        """Возвращает систему охлаждения по id. Детальная информация о системе охлаждения."""
        return await super().retrieve(request)
