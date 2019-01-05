from django.urls import path
from . import views

urlpatterns = [
    path('', views.ecg_list, name='ecg_list'),
]
