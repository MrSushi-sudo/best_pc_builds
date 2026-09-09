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


class MotherboardSerializer(BaseComponentSerializer):
    """Сериализатор для материнских плат"""

    socket: str
    chipset: str
    form_factor: str
    memory_type: str
    memory_slots: int
    max_memory: int


class VideoCardSerializer(BaseComponentSerializer):
    """Сериализатор для видеокарт"""

    chipset: str
    memory_size: int
    memory_type: str
    length_mm: int | None
    tdp: int | None


class RamSerializer(BaseComponentSerializer):
    """Сериализатор для оперативной памяти"""

    memory_type: str
    total_capacity: int
    modules_count: int
    frequency: int
    latency_cl: int


class StorageSerializer(BaseComponentSerializer):
    """Сериализатор для накопителей"""

    storage_type: str
    capacity: int
    interface: str
    read_speed: int | None
    write_speed: int | None


class PowerSupplySerializer(BaseComponentSerializer):
    """Сериализатор для блоков питания"""

    power: int
    efficiency: str
    modular: bool
    form_factor: str


class ComputerCaseSerializer(BaseComponentSerializer):
    """Сериализатор для корпусов"""

    form_factor: str
    max_gpu_length: int | None
    max_cooler_height: int | None


class CoolingSystemSerializer(BaseComponentSerializer):
    """Сериализатор для систем охлаждения"""

    cooler_type: str
    socket_support: str
    fan_size: int | None
    tdp: int | None
