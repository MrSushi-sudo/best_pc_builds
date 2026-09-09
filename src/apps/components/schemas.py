from uuid import UUID

from django_bolt.serializers import Serializer


class BaseComponentSerializer(Serializer):
    """Сериализатор для базовых компонентов"""

    id: UUID
    name: str
    manufacturer: str
    price: float | None


class ProcessorSerializer(BaseComponentSerializer):
    """Сериализатор для процессоров"""

    socket: str
    cores: int
    threads: int
    base_clock: float
    turbo_clock: float
    tdp: int
