from django.urls import path

from . import views

app_name = 'links'

urlpatterns = [
    path('', views.index, name='list'),
    path('add/', views.add, name='add'),
    path('edit/<int:link_id>/', views.edit, name='edit'),
]
