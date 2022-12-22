from rest_framework import serializers
from news.models import New


class NewSerializer(serializers.ModelSerializer):
    """ModelSerializer of New Model"""

    class Meta:
        model = New
        fields = (
            "title",
            "content",
            "create_date",
            "upgrade_date",
        )
