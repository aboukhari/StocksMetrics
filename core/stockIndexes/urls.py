from django.urls import path
from . import views

urlpatterns = [
    path('index', views.stock_table, name='index'),
]