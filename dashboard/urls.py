from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('orderhistory/', views.orderhistory, name='orderhistory'),
    path('sessionDetailsManager/', views.sessionDetailsManager, name="sessionDetailsManager"),
    path('getNewOrderManager/', views.getNewOrderManager, name="getNewOrderManager"),
    path('deleteorder/', views.deleteOrder, name="delete"),
    path('getWaiterCall/', views.getWaiterCall, name="getWaiterCall"),
	path('deletewaiter/', views.deletewaiter, name="deletewaiter"),
	
	path('neworderwaiter/', views.neworderwaiter, name="neworderwaiter"),
	path('shiftcooking/', views.shiftcooking, name="shiftcooking"),
    path('served/', views.served, name="served"),
    
    path('shifttocookingmanager/', views.shifttocookingmanager, name="shifttocookingmanager"),
    path('shifttoservedmanager/', views.shifttoservedmanager, name="shifttoservedmanager"),
    path('verifypaymenttable/', views.verifypaymenttable, name="verifypaymenttable"),
    path('shifttoverified/', views.shifttoverified, name="shifttoverified"),


] 