from django.contrib import admin
from django.http import HttpRequest

from apps.offers.models import MarketplaceOffer, MarketplacePriceSnapshot


class MarketplacePriceSnapshotInline(admin.TabularInline):
    model = MarketplacePriceSnapshot
    extra = 0
    readonly_fields = ("price", "regular_price", "status", "fetched_at")
    fields = ("price", "regular_price", "status", "fetched_at")
    can_delete = False

    def has_add_permission(self, request: HttpRequest, obj=None) -> bool:
        print(type(obj))
        return False


@admin.register(MarketplaceOffer)
class MarketplaceOfferAdmin(admin.ModelAdmin):
    list_display = (
        "marketplace",
        "title",
        "seller_name",
        "current_price",
        "currency",
        "status",
        "active",
        "last_success_at",
    )
    list_filter = ("marketplace", "status", "active", "currency", "region")
    search_fields = ("title", "seller_name", "external_id", "url")
    readonly_fields = (
        "created",
        "updated",
        "last_seen_at",
        "last_success_at",
        "last_error",
        "raw_data",
    )
    inlines = (MarketplacePriceSnapshotInline,)


@admin.register(MarketplacePriceSnapshot)
class MarketplacePriceSnapshotAdmin(admin.ModelAdmin):
    list_display = ("offer", "price", "regular_price", "status", "fetched_at")
    list_filter = ("status", "offer__marketplace")
    search_fields = (
        "offer__title",
        "offer__seller_name",
        "offer__external_id",
        "offer__url",
    )
    readonly_fields = (
        "offer",
        "price",
        "regular_price",
        "status",
        "fetched_at",
        "raw_data",
    )
