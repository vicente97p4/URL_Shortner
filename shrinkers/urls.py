"""shrinkers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
import debug_toolbar
from django.conf.urls import include
from shortener.views import index, get_user, register, login_view, logout_view
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    # include 함수는 뒤에 여러가지 endpoint가 있을 때 한꺼번에 결합해줄 때 쓴다.
    path("__debug__/", include(debug_toolbar.urls)),  # Django Debug Tool
    path("", index, name="index"),
    path('register/', register, name='register'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path("get_user/<int:user_id>", get_user),
]
