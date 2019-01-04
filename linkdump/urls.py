"""linkdump URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
from django.urls import include, path

import links.urls


def redirect_home(request):
    # Check if user is logged in.
    if request.user.is_authenticated:
        return redirect('links')
    return redirect('auth-login')


urlpatterns = [
    path(r'', redirect_home),
    path(r'links/', include(links.urls.urlpatterns)),
    path(r'auth/login/', auth_views.LoginView.as_view(), name='auth-login'),
    path(r'auth/logout/', auth_views.LogoutView.as_view(), name='auth-logout'),
    path(r'admin/', admin.site.urls),
]
