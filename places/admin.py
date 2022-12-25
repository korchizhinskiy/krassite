from django.contrib import admin
from places.models import Place
from import_export.admin import ImportExportActionModelAdmin


@admin.register(Place)
class PlaceAdmin(ImportExportActionModelAdmin):
    class Meta:
        model = Place

    list_display = (
        "name",
        "longitude",
        "latitude",
        "rating",
    )
