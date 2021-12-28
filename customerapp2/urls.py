from django.urls import path,include
from . import views
from django.conf import settings

urlpatterns = [
	# from table qrcode:
	path('redirect', views.redirect, name='redirect'),

	# from waiter qrcode:
	path('<int:restaurantidslug>/<int:tableno>/welcome/', views.welcome, name='welcome'),
	path('<int:restaurantidslug>/<int:tableno>/menu/', views.customerapp, name='customerapp'),



	path('<int:restaurantidslug>/<int:tableno>/<slug:hashcode>/status/', views.status, name='status'),
	path('<int:restaurantidslug>/<int:tableno>/<slug:hashcode>/feedback/', views.feedback, name='feedback'),
	path('<int:restaurantidslug>/<int:tableno>/<slug:hashcode>/checkout/', views.checkout, name='checkout'),
	path('<int:restaurantidslug>/<int:tableno>/<slug:hashcode>/payment/', views.payment, name='payment'),
	path('accounts/', include('allauth.urls')),
	path('<int:restaurantidslug>/<int:tableno>/<slug:hashcode>/callwaiter/', views.callwaiter, name='callwaiter'),
]
