from django.urls import path

from . import views

app_name = 'links'

urlpatterns = [
    path(r'', views.index, name='links'),
    path(r'add/', views.add, name='links-add'),
    path(r'edit/<int:link_id>/', views.edit, name='links-edit'),
]
