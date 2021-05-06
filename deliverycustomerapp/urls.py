from django.urls import path,include
from . import views
from django.conf import settings

urlpatterns = [
	path('<int:restaurantidslug>/', views.deliverycustomerapp, name='deliverycustomerapp'),
	path('<int:restaurantidslug>/checkout/', views.checkout, name='checkout'),
	path('<int:restaurantidslug>/address/', views.address, name='address'),
	path('<int:restaurantidslug>/thankyou/', views.thankyou, name='thankyou'),

	# path('<int:restaurantidslug>/<int:tableno>/<slug:hashcode>/status/', views.status, name='status'),
	# path('<int:restaurantidslug>/<int:tableno>/<slug:hashcode>/feedback/', views.feedback, name='feedback'),
	# path('<int:restaurantidslug>/<int:tableno>/<slug:hashcode>/checkout/', views.checkout, name='checkout'),
	# 
	# path('accounts/', include('allauth.urls')),
	# path('<int:restaurantidslug>/<int:tableno>/<slug:hashcode>/callwaiter/', views.callwaiter, name='callwaiter'),
]