from django.http import HttpResponse
from rest_framework import viewsets
from news import tasks
from news.serializers import NewSerializer
from news.models import New


def home(request):
    tasks.send_mail_task.delay()
    return HttpResponse('<h1>Проверьте почту</h1>')


class NewViewSet(viewsets.ModelViewSet):
    """ModelViewSet for New Model"""
    serializer_class = NewSerializer

    def get_queryset(self):
        return New.objects.all()
