from django.urls import path

from . import views

urlpatterns = [
    path('file/<int:pk>/', views.LoadFile, name='LoadFile')
]