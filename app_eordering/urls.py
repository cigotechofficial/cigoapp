from django.urls import path,include
from . import views
from django.conf import settings

urlpatterns = [
	# from table qrcode:
	path('redirect', views.redirect, name='redirect'),

	# from waiter qrcode:
	path('<int:restaurantidslug>/<int:tableno>/<slug:hashcode>/welcome/', views.welcome, name='welcome'),
	path('<int:restaurantidslug>/<int:tableno>/<slug:hashcode>/menu/', views.customerapp, name='customerapp'),



	path('<int:restaurantidslug>/<int:tableno>/<slug:hashcode>/status/', views.status, name='status'),
	path('<int:restaurantidslug>/<int:tableno>/<slug:hashcode>/feedback/', views.feedback, name='feedback'),
	path('<int:restaurantidslug>/<int:tableno>/<slug:hashcode>/checkout/', views.checkout, name='checkout'),
	path('<int:restaurantidslug>/<int:tableno>/<slug:hashcode>/payment/', views.payment, name='payment'),
	path('accounts/', include('allauth.urls')),
	path('<int:restaurantidslug>/<int:tableno>/<slug:hashcode>/callwaiter/', views.callwaiter, name='callwaiter'),
]

# urlpatterns = [
#     path('<int:restaurantidslug>/', views.logingmail, name='logingmail'),
#     path('redirect', views.redirect, name='redirect'),
#     path('logoutgoogle', views.logoutgoogle, name='logoutgoogle'),
#     path('<int:restaurantidslug>/activationqr/', views.activationqr, name='activationqr'),
#     path('<int:restaurantidslug>/<int:tableno>/menu/', views.customerapp, name='customerapp'),
#     path('<int:restaurantidslug>/<int:tableno>/status/', views.status, name='status'),
#     path('<int:restaurantidslug>/<int:tableno>/feedback/', views.feedback, name='feedback'),
#     path('<int:restaurantidslug>/<int:tableno>/addfeedback/', views.addfeedback, name='addfeedback'),
#     path('<int:restaurantidslug>/<int:tableno>/checkout/', views.checkout, name='checkout'),
#     path('<int:restaurantidslug>/<int:tableno>/payment/', views.payment, name='payment'),
#     path('accounts/', include('allauth.urls')),

#     path('<int:restaurantidslug>/<int:tableno>/callwaiter/', views.callwaiter, name='callwaiter'),
# ]