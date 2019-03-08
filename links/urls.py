from django.urls import path

from . import views

app_name = 'links'

urlpatterns = [
    path('', views.Index.as_view(), name='list'),
    path('add/', views.Add.as_view(), name='add'),
    path('edit/<int:link_id>/', views.edit, name='edit'),
]
