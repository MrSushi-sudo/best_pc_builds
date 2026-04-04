from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.best_pc_builds.mixins import TimeStampedMixin, UUID8Mixin


class BaseComponent(UUID8Mixin, TimeStampedMixin):
    """Миксин для базовых компонентов"""

    name = models.CharField(verbose_name=_("Название"), max_length=255)
    manufacturer = models.CharField(verbose_name=_("Производитель"), max_length=255)
    price = models.DecimalField(verbose_name=_("Цена"), max_digits=12, decimal_places=2, null=True, blank=True)

    class Meta:
        abstract = True
        ordering = ("-created",)

    def __str__(self) -> str:
        return self.name
