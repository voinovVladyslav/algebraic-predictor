from django.urls import path

from . import views


urlpatterns = [
    path('int/', views.counter, name='counter'),
    path('', views.console, name='console'),
]
