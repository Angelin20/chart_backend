from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from . import views

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]