"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    path('current_datetime/', views.current_datetime, name='current_datetime'),
    path('item_list/', views.item_list, name='item_list'),
    # path('home/',views.home, name='home'),

    path('',views.store, name='store'),
    path('login_page/',views.login, name='login_page'),
    path('logout/',views.logout_view, name='logout'),
    path('register/',views.register, name='register'),
    path('cart/',views.cart, name='cart'),
    path('storeAdmin/',views.storeAdmin, name='storeAdmin'),

    # path('user_login/',views.user_login, name='user_login'),

]\
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
