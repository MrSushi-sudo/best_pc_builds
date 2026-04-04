from django.contrib import admin

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


@admin.register(Processor)
class ProcessorAdmin(admin.ModelAdmin):
    pass


@admin.register(Motherboard)
class MotherboardAdmin(admin.ModelAdmin):
    pass


@admin.register(VideoCard)
class VideoCardAdmin(admin.ModelAdmin):
    pass


@admin.register(Ram)
class RamAdmin(admin.ModelAdmin):
    pass


@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    pass


@admin.register(PowerSupply)
class PowerSupplyAdmin(admin.ModelAdmin):
    pass


@admin.register(ComputerCase)
class ComputerCaseAdmin(admin.ModelAdmin):
    pass


@admin.register(CoolingSystem)
class CoolingSystemAdmin(admin.ModelAdmin):
    pass

