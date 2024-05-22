from django.forms import model_to_dict  # импорт спец функции, преобразовывает объект в словарь
from django.shortcuts import render
from rest_framework import generics, viewsets  # импорт generics
from rest_framework.response import Response  # импорт response
from rest_framework.views import APIView  # импорт базового класса APIView

from .models import Women  # импорт Women
from .serializers import WomenSerializer


class WomenViewSet(viewsets.ModelViewSet):  # Класс от ModelViewSet для CRUD
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


# class WomenAPIList(generics.ListCreateAPIView):  # ListCreateAPIView - чтение данных (GET) и добавление (POST-запрос)
#     queryset = Women.objects.all()  # атрибут ссылается на список записей, возвращаемый клиенту
#     serializer_class = WomenSerializer  # сериализатор применяется к queryset
#
#
# class WomenAPIUpdate(generics.UpdateAPIView):  # Изменение данных (PUT, PATCH-запросы)
#     queryset = Women.objects.all()  # Клиенту возвращаются не все записи, а только измененные (ленивый запрос)
#     serializer_class = WomenSerializer
#
#
# class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):  # GET, PUT, PATCH, DELETE-запросы (CRUD)
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

