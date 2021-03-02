from django.contrib import admin
from django.urls import path,include
from accounts import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('home/', include('home.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('setup/', include('setup.urls')),
    path('help/', include('help.urls')),
    path('customerapp/', include('customerapp.urls')),
    path('signup', views.handleSignup, name='handleSignup'),
    path('login', views.handleLogin, name='handleLogin'),
    path('logout', views.handleLogout, name='handleLogout'),
    path('changePassword', views.changePassword, name='changePassword'), 
    

]
 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 