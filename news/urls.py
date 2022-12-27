from django.urls import include, path
from rest_framework import routers

from news.views import NewViewSet, home


router = routers.SimpleRouter()
router.register(r"new", NewViewSet, basename="news")

urlpatterns = [
    path('api/', include(router.urls)),
    path('send_mail/', home, name="home")
]
