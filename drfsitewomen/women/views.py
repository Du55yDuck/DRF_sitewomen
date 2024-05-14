from django.shortcuts import render
from rest_framework import generics  # импорт generics
from .models import Women  # импорт Women
from .serializers import WomenSerializer


class WomenAPIView(generics.ListAPIView):  # Базовый класс представления
    queryset = Women.objects.all()  # взять все записи из таблицы Women
    serializer_class = WomenSerializer  # класс сериализатора
