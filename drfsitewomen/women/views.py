from django.forms import model_to_dict  # импорт спец функции, преобразовывает объект в словарь
from django.shortcuts import render
from rest_framework import generics  # импорт generics
from rest_framework.response import Response  # импорт response
from rest_framework.views import APIView  # импорт базового класса APIView

from .models import Women  # импорт Women
from .serializers import WomenSerializer


class WomenAPIView(APIView):  # Базовый класс наследуем от APIView
    def get(self, request):  # обработка параметров get запросов
        w = Women.objects.all()  # прочесть все данные из таблицы Women(queryset) - список статей
        return Response({'posts': WomenSerializer(w, many=True).data})  # возвращает клиенту json-строку(список записей)

    def post(self, request):  # обработка post запросов, позволяет добавлять новые данные в бд
        serializer = WomenSerializer(data=request.data)  # сериализатор на основе данных из POST-запроса
        serializer.is_valid(raise_exception=True)  # проверка на корректность, данные WomenSerializer и вывод исключения

        post_new = Women.objects.create(  # ссылка на новую запись в таблице Women (сохранение данных в бд)
            title=request.data['title'],  # обязательные поля --> ссылки на значение одноименного ключа
            content=request.data['content'],
            cat_id=request.data['cat_id'],
        )
        return Response({'post': WomenSerializer(post_new).data})  # возвращает клиенту, добавленное значение в бд


# class WomenAPIView(generics.ListAPIView):  # Базовый класс представления
#     queryset = Women.objects.all()  # взять все записи из таблицы Women
#     serializer_class = WomenSerializer  # класс сериализатора
