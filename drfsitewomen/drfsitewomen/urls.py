"""
URL configuration for drfsitewomen project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include, re_path

from women.views import *
from rest_framework import routers  # импорт роутер

# router = routers.DefaultRouter() #Объект роутер от DefaultRouter. Можно импорт и подключить кастомный ро-р(routers.py)
# router.register(r'women', WomenViewSet, basename='women')  # регистрация в роутере класс WomenViewSet + префикс women

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/v1/', include(router.urls)),  # генерация всех urls через роутер + http://127.0.0.1:8000/api/v1/women
    path('api/v1/drf-auth/', include('rest_framework.urls')),  # подключение авторизации ДРФ
    path('api/v1/women/', WomenAPIList.as_view()),  # маршрут получения списка статей
    path('api/v1/women/<int:pk>/', WomenAPIUpdate.as_view()),  # маршрут изменения записи
    path('api/v1/womendelete/<int:pk>/', WomenAPIDestroy.as_view()),  # маршрут удаления записи
    path('api/v1/auth/', include('djoser.urls')),  # маршрут для djoser
    re_path(r'^auth/', include('djoser.urls.authtoken')),  # re_path для использования регулярок (r'...)  в URL
]
