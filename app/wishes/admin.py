"""Admin config. Delete a wish here if one ever needs to come down."""

from django.contrib import admin

from .models import WellWish


@admin.register(WellWish)
class WellWishAdmin(admin.ModelAdmin):
    """Admin list with search."""

    list_display = ("name", "relationship", "message", "created")
    search_fields = ("name", "message")
