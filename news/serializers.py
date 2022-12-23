from rest_framework import serializers
from news.models import New


class NewSerializer(serializers.ModelSerializer):
    """ModelSerializer of New Model"""
    preview_image = serializers.ImageField(read_only=True)

    class Meta:
        model = New
        fields = (
            "id",
            "title",
            "content",
            "create_date",
            "upgrade_date",
            "image",
            "preview_image",
            "author",
        )
