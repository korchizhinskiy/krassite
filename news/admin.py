from django.contrib import admin
from news.models import New


@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    """New Admin Model"""
    list_display = (
        "title",
        "content",
        "create_date",
        "upgrade_date",
        "image",
        "preview_image",
        "author",
    )
    exclude = ("preview_image",)
