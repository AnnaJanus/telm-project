from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.ecg_list, name='ecg_list'),
    url(r'^line_chart/$', views.line_chart_json, name='line_chart_json'),
]
