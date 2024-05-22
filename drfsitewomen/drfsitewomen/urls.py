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
from django.urls import path, include

from women.views import *
from rest_framework import routers  # импорт роутер

router = routers.SimpleRouter()  # объект роутер от SimpleRouter
router.register(r'women', WomenViewSet)  # регистрация в роутере класс WomenViewSet + префикс women

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),  # генерация всех urls через роутер + http://127.0.0.1:8000/api/v1/women
    # path('api/v1/womenlist/', WomenViewSet.as_view({'get': 'list'})),  # маршрут WomenViewSet + 'get': 'list'
    # path('api/v1/womenlist/<int:pk>/', WomenViewSet.as_view({'put': 'update'})),  # маршрут для CRUD + put...
]  # в словарях указываются методы запросов и методы самих операций (см доку)



