from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.deliverydashboard, name='deliverydashboard'),
    path('getNewDeliveryOrder/', views.getNewDeliveryOrder, name="getNewDeliveryOrder"),
    path('deliverydiscount/', views.deliverydiscount, name="deliverydiscount"),

    path('shifttodelivery/', views.shifttodelivery, name="shifttodelivery"),
    path('deletedelivery/', views.deletedelivery, name="deletedelivery"),


] 