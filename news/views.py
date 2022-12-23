from rest_framework import viewsets
from news.serializers import NewSerializer
from news.models import New


class NewViewSet(viewsets.ModelViewSet):
    """ModelViewSet for New Model"""
    serializer_class = NewSerializer

    def get_queryset(self):
        return New.objects.all()
