from django.contrib import admin
from news.models import New
from django_summernote.admin import SummernoteModelAdmin


@admin.register(New)
class NewAdmin(SummernoteModelAdmin):
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
    summernote_fields = (
        "title",
        "content",
    )
