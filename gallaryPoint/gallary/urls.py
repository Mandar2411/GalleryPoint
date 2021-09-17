from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallary, name='album'),
    path('photo/<str:pk>/', views.viewPhoto, name='photo'),
    path('add/', views.addPhoto, name='add'),
]