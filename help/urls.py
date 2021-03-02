from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
path('tutorials/', views.tutorials, name='tutorials'),
path('productspecialist/', views.productspecialist, name='productspecialist'),
path('call/', views.call, name='call'),
]