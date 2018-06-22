from django.urls import path

from . import views

app_name = 'links'

urlpatterns = [
    path(r'', views.index, name='index'),
]
