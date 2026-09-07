from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from apps.best_pc_builds.mixins import ActiveMixin, TimeStampedMixin, UUID8Mixin


class MarketplaceChoices(models.TextChoices):
    """Поддерживаемые маркетплейсы."""

    WILDBERRIES = "WILDBERRIES", _("Wildberries")
    OZON = "OZON", _("Ozon")
    YANDEX_MARKET = "YANDEX_MARKET", _("Яндекс Маркет")


class OfferStatusChoices(models.TextChoices):
    """Статус доступности оффера на маркетплейсе."""

    AVAILABLE = "AVAILABLE", _("В наличии")
    OUT_OF_STOCK = "OUT_OF_STOCK", _("Нет в наличии")
    NOT_FOUND = "NOT_FOUND", _("Не найден")
    ERROR = "ERROR", _("Ошибка парсинга")


class MarketplaceOffer(UUID8Mixin, TimeStampedMixin, ActiveMixin):
    """Оффер комплектующего на конкретном маркетплейсе."""

    component_content_type = models.ForeignKey(
        to=ContentType,
        verbose_name=_("Тип комплектующего"),
        on_delete=models.CASCADE,
    )
    component_object_id = models.UUIDField(verbose_name=_("id комплектующего"), db_index=True)
    component = GenericForeignKey("component_content_type", "component_object_id")

    marketplace = models.CharField(verbose_name=_("Маркетплейс"), max_length=32, choices=MarketplaceChoices.choices)
    external_id = models.CharField(verbose_name=_("Внешний id"), max_length=128, blank=True)
    url = models.URLField(verbose_name=_("Ссылка"), max_length=1000)

    title = models.CharField(verbose_name=_("Название у продавца"), max_length=500, blank=True)
    seller_id = models.CharField(verbose_name=_("id продавца"), max_length=128, blank=True)
    seller_name = models.CharField(verbose_name=_("Продавец"), max_length=255, blank=True)
    region = models.CharField(verbose_name=_("Регион"), max_length=64, default="RU")

    current_price = models.DecimalField(
        verbose_name=_("Текущая цена"),
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True,
    )
    regular_price = models.DecimalField(
        verbose_name=_("Цена без скидки"),
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True,
    )
    currency = models.CharField(verbose_name=_("Валюта"), max_length=3, default="RUB")

    status = models.CharField(verbose_name=_("Статус"), max_length=32, choices=OfferStatusChoices.choices)

    last_seen_at = models.DateTimeField(verbose_name=_("Последняя проверка"), null=True, blank=True)
    last_success_at = models.DateTimeField(verbose_name=_("Последняя успешная проверка"), null=True, blank=True)
    last_error = models.TextField(verbose_name=_("Последняя ошибка"), blank=True)
    raw_data = models.JSONField(verbose_name=_("Сырые данные"), default=dict, blank=True)

    class Meta:
        verbose_name = _("Оффер маркетплейса")
        verbose_name_plural = _("Офферы маркетплейсов")
        ordering = ("current_price", "-updated")
        constraints = (
            models.UniqueConstraint(
                fields=("marketplace", "external_id", "region"),
                condition=~models.Q(external_id=""),
                name="unique_offer_by_external_id",
            ),
            models.UniqueConstraint(
                fields=("marketplace", "url", "region"),
                name="unique_offer_by_url",
            ),
            models.CheckConstraint(
                condition=models.Q(current_price__gte=0) | models.Q(current_price__isnull=True),
                name="offer_current_price_gte_0",
            ),
            models.CheckConstraint(
                condition=models.Q(regular_price__gte=0) | models.Q(regular_price__isnull=True),
                name="offer_regular_price_gte_0",
            ),
        )
        indexes = (
            models.Index(fields=("component_content_type", "component_object_id")),
            models.Index(fields=("marketplace", "status", "active")),
            models.Index(fields=("current_price",)),
        )

    def __str__(self) -> str:
        return f"{self.get_marketplace_display()}: {self.title or self.url}"


class MarketplacePriceSnapshot(UUID8Mixin):
    """Снимок цены оффера после очередного парсинга."""

    offer = models.ForeignKey(
        to=MarketplaceOffer,
        verbose_name=_("Оффер"),
        related_name="price_snapshots",
        on_delete=models.CASCADE,
    )
    price = models.DecimalField(verbose_name=_("Цена"), max_digits=12, decimal_places=2, null=True, blank=True)
    regular_price = models.DecimalField(
        verbose_name=_("Цена без скидки"),
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True,
    )
    status = models.CharField(verbose_name=_("Статус"), max_length=32, choices=OfferStatusChoices.choices)
    fetched_at = models.DateTimeField(verbose_name=_("Дата парсинга"), default=timezone.now)
    raw_data = models.JSONField(verbose_name=_("Сырые данные"), default=dict, blank=True)

    class Meta:
        verbose_name = _("Снимок цены")
        verbose_name_plural = _("Снимки цен")
        ordering = ("-fetched_at",)
        constraints = (
            models.CheckConstraint(
                condition=models.Q(price__gte=0) | models.Q(price__isnull=True),
                name="price_snapshot_price_gte_0",
            ),
            models.CheckConstraint(
                condition=models.Q(regular_price__gte=0) | models.Q(regular_price__isnull=True),
                name="price_snapshot_regular_price_gte_0",
            ),
        )
        indexes = (
            models.Index(fields=("offer", "-fetched_at")),
            models.Index(fields=("-fetched_at",)),
        )

    def __str__(self) -> str:
        return f"{self.offer} - {self.price} {self.offer.currency}"
