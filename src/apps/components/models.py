from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.components.mixins import BaseComponent


class MemoryTypeChoices(models.TextChoices):
    DDR4 = 'DDR4', _('DDR4')
    DDR5 = 'DDR5', _('DDR5')


class FormFactorChoices(models.TextChoices):
    ATX = 'ATX', _('ATX')
    MICRO_ATX = 'Micro-ATX', _('Micro-ATX')
    MINI_ITX = 'Mini-ITX', _('Mini-ITX')
    E_ATX = 'E-ATX', _('E-ATX')


class StorageTypeChoices(models.TextChoices):
    HDD = 'HDD', _('HDD')
    SSD_SATA = 'SSD_SATA', _('SSD SATA')
    SSD_NVME = 'SSD_NVME', _('SSD NVMe')


class CoolerTypeChoices(models.TextChoices):
    AIR = 'AIR', _('Воздушное')
    LIQUID = 'LIQUID', _('Жидкостное')


class Processor(BaseComponent):
    """Модель процессоров"""
    socket = models.CharField(verbose_name=_('Сокет'), max_length=32)
    cores = models.PositiveSmallIntegerField(verbose_name=_('Количество ядер'))
    threads = models.PositiveSmallIntegerField(verbose_name=_('Количество потоков'))
    base_clock = models.DecimalField(verbose_name=_('Базовая частота, ГГц'), max_digits=4, decimal_places=2)
    turbo_clock = models.DecimalField(verbose_name=_('Турбо-частота, ГГц'), max_digits=4, decimal_places=2)
    tdp = models.PositiveSmallIntegerField(verbose_name=_('Теплопакет, Вт'))

    class Meta:
        verbose_name = _('Процессор')
        verbose_name_plural = _('Процессоры')
        ordering = ('-created',)


class Motherboard(BaseComponent):
    """Модель мат.плат"""
    socket = models.CharField(verbose_name=_('Сокет'), max_length=32)
    chipset = models.CharField(verbose_name=_('Чипсет'), max_length=64)
    form_factor = models.CharField(verbose_name=_('Форм-фактор'), max_length=16, choices=FormFactorChoices.choices)
    memory_type = models.CharField(verbose_name=_('Тип памяти'), max_length=8, choices=MemoryTypeChoices.choices)
    memory_slots = models.PositiveSmallIntegerField(verbose_name=_('Слоты памяти'))
    max_memory = models.PositiveSmallIntegerField(verbose_name=_('Максимум памяти, ГБ'))

    class Meta:
        verbose_name = _('Материнская плата')
        verbose_name_plural = _('Материнские платы')
        ordering = ('-created',)


class VideoCard(BaseComponent):
    """Модель видеокарт"""
    chipset = models.CharField(verbose_name=_('Графический процессор'), max_length=128)
    memory_size = models.PositiveSmallIntegerField(verbose_name=_('Объём видеопамяти, ГБ'))
    memory_type = models.CharField(verbose_name=_('Тип видеопамяти'), max_length=32)
    length_mm = models.PositiveSmallIntegerField(verbose_name=_('Длина, мм'), null=True, blank=True)
    tdp = models.PositiveSmallIntegerField(verbose_name=_('Теплопакет, Вт'), null=True, blank=True)

    class Meta:
        verbose_name = _('Видеокарта')
        verbose_name_plural = _('Видеокарты')
        ordering = ('-created',)


class Ram(BaseComponent):
    """Модель оперативной памяти"""
    memory_type = models.CharField(verbose_name=_('Тип памяти'), max_length=8, choices=MemoryTypeChoices.choices)
    total_capacity = models.PositiveIntegerField(verbose_name=_('Общий объём, ГБ'))
    modules_count = models.PositiveSmallIntegerField(verbose_name=_('Количество модулей'), default=1)
    frequency = models.PositiveIntegerField(verbose_name=_('Частота, МГц'))
    latency_cl = models.PositiveSmallIntegerField(verbose_name=_('Тайминг CL'))

    class Meta:
        verbose_name = _('Оперативная память')
        verbose_name_plural = _('Оперативная память')
        ordering = ('-created',)


class Storage(BaseComponent):
    """Модель накопителей"""
    storage_type = models.CharField(verbose_name=_('Тип накопителя'), max_length=16, choices=StorageTypeChoices.choices)
    capacity = models.PositiveIntegerField(verbose_name=_('Объём, ГБ'))
    interface = models.CharField(verbose_name=_('Интерфейс'), max_length=32)
    read_speed = models.PositiveIntegerField(verbose_name=_('Скорость чтения, МБ/с'), null=True, blank=True)
    write_speed = models.PositiveIntegerField(verbose_name=_('Скорость записи, МБ/с'), null=True, blank=True)

    class Meta:
        verbose_name = _('Накопитель')
        verbose_name_plural = _('Накопители')
        ordering = ('-created',)


class PowerSupply(BaseComponent):
    """Модель блоков питания"""
    power = models.PositiveSmallIntegerField(verbose_name=_('Мощность, Вт'))
    efficiency = models.CharField(verbose_name=_('Сертификат эффективности'), max_length=32)
    modular = models.BooleanField(verbose_name=_('Модульный'), default=False)
    form_factor = models.CharField(verbose_name=_('Форм-фактор'), max_length=16, choices=FormFactorChoices.choices)

    class Meta:
        verbose_name = _('Блок питания')
        verbose_name_plural = _('Блоки питания')
        ordering = ('-created',)


class ComputerCase(BaseComponent):
    """Модель корпусов"""
    form_factor = models.CharField(verbose_name=_('Форм-фактор'), max_length=16, choices=FormFactorChoices.choices)
    max_gpu_length = models.PositiveSmallIntegerField(verbose_name=_('Максимальная длина видеокарты, мм'), null=True, blank=True)
    max_cooler_height = models.PositiveSmallIntegerField(verbose_name=_('Максимальная высота кулера, мм'), null=True, blank=True)

    class Meta:
        verbose_name = _('Корпус')
        verbose_name_plural = _('Корпуса')
        ordering = ('-created',)


class CoolingSystem(BaseComponent):
    """Модель систем охлаждения"""
    cooler_type = models.CharField(verbose_name=_('Тип охлаждения'), max_length=16, choices=CoolerTypeChoices.choices)
    socket_support = models.CharField(verbose_name=_('Поддерживаемые сокеты'), max_length=255)
    fan_size = models.PositiveSmallIntegerField(verbose_name=_('Размер вентилятора, мм'), null=True, blank=True)
    tdp = models.PositiveSmallIntegerField(verbose_name=_('Рассеиваемая мощность, Вт'), null=True, blank=True)

    class Meta:
        verbose_name = _('Система охлаждения')
        verbose_name_plural = _('Системы охлаждения')
        ordering = ('-created',)
