# produtores/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.produtor_list, name='produtor_list'),
    path('produtor/new/', views.produtor_create, name='produtor_create'),
    path('produtor/<int:pk>/edit/', views.produtor_update, name='produtor_update'),
    path('produtor/<int:pk>/delete/', views.produtor_delete, name='produtor_delete'),
]