from django_bolt.serializers import Serializer


class BaseComponentSerializer(Serializer):
    """Сериализатор для базовых компонентов"""

    name: str
    manufacturer: str
    price: float


class ProcessorSerializer(BaseComponentSerializer):
    """Сериализатор для процессоров"""

    socket: str
    cores: int
    threads: int
    base_clock: float
    turbo_clock: int
    tdp: int
