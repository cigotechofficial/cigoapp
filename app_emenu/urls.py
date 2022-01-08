from django.urls import path,include
from . import views
from django.conf import settings

urlpatterns = [
	path('<int:restaurantidslug>/welcome/', views.welcome, name='welcome'),
	path('<int:restaurantidslug>/menu/', views.emenu, name='emenu'),
	
]