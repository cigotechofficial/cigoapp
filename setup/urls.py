from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.setup, name='setup'),
    path('newvenue', views.newvenue, name='newvenue'),
    path('editvenue', views.editvenue, name='editvenue'),
    path('deletevenue', views.deletevenue, name='deletevenue'),
    path('addemployee', views.addemployee, name='addemployee'),
    path('editemployee', views.editemployee, name='editemployee'),
    path('deleteemployee', views.deleteemployee, name='deleteemployee'),
    path('menupage/', views.menupage, name='menupage'),
    path('additem/', views.additem, name='additem'),
    path('updatemenu/', views.updatemenu, name='updatemenu'),
    path('updateimg/', views.updateimg, name='updateimg'),
    path('menupage/deletemenu/', views.deletemenu, name='deletemenu'),
    path('menupage/venueselect/', views.venueselect, name='venueselect'),

] 
