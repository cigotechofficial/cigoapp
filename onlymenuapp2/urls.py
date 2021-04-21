from django.urls import path,include
from . import views
from django.conf import settings

urlpatterns = [
	path('<int:restaurantidslug>/welcome2/', views.welcome, name='welcome'),
	path('<int:restaurantidslug>/menu2/', views.customerapp, name='customerapp'),
	
]