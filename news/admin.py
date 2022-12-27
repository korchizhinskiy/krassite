from django.contrib import admin
from django.utils.safestring import mark_safe
from news.models import Contact, New
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
    )


@admin.register(New)
class NewAdmin(SummernoteModelAdmin):
    """New Admin Model"""
    list_display = (
        "get_title_by_html_render",
        "create_date",
        "upgrade_date",
        "image",
        "preview_image",
        "author",
    )
    search_fields = (
        "title",
    )
    search_help_text = "Введите название публикации"
    exclude = (
        "preview_image",
    )
    summernote_fields = (
        "title",
        "content",
    )

    @admin.display(description="Заголовок")
    def get_title_by_html_render(self, new):
        """Get title with html rendering by summernote app"""
        return mark_safe(new.title)

    @admin.display(description="Контент")
    def get_content_by_html_render(self, new):
        """
        Get content with html rendering by summernote app.
        Use only with truncate words.
        """
        return mark_safe(new.content)
