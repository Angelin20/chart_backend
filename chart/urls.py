from django.urls import path

from . import views

urlpatterns = [
    path('', views.ChartList.as_view()),
    path('<int:pk>/', views.ChartDetail.as_view())
]