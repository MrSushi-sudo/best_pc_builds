import uuid6
from django.db import models
from django.utils.translation import gettext_lazy as _


class CreatedMixin(models.Model):
    """Миксин даты создания"""

    created = models.DateTimeField(verbose_name=_("Дата создания"), auto_now_add=True)

    class Meta:
        abstract = True


class TimeStampedMixin(models.Model):
    """Миксин даты создания и изменения"""

    created = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Дата изменения", auto_now=True)

    class Meta:
        abstract = True


class WeightMixin(models.Model):
    """Миксин веса"""

    weight = models.PositiveIntegerField(verbose_name=_("Вес при сортировке"), default=1)

    class Meta:
        abstract = True


class ActiveMixin(models.Model):
    """Миксин активности"""

    active = models.BooleanField(verbose_name=_("Активен"), default=False)

    class Meta:
        abstract = True


class UUID8Mixin(models.Model):
    """Миксин primary key UUID8"""

    id = models.UUIDField(primary_key=True, default=uuid6.uuid8, editable=False, verbose_name=_("id"))

    class Meta:
        abstract = True
