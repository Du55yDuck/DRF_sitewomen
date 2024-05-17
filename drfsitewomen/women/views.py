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
        serializer.save()  # метод вызывает create и сохраняет новую запись в бд.

        return Response({'post': serializer.data})  # возвращает клиенту, добавленное значение в бд

    def put(self, request, *args, **kwargs):  # метод с аргументами -
        pk = kwargs.get("pk", None)  # через kwargs берет ключ pk, иначе None
        if not pk:  # проверка на наличие pk + ответ клиенту, если pk не найден в URL
            return Response({"error": "Method PUT not allowed"})

        try:  # проверка на наличие ключа pk в модели Women
            instance = Women.objects.get(pk=pk)
        except:  # если ключа pk нет в таблице, тогда вывод ответа об ошибке
            return Response({"error": "Object does not exists"})

        serializer = WomenSerializer(data=request.data, instance=instance)  # создать объект сериализатор и передать
        # в него данные для изменения и объект instance (запись для изменений)
        serializer.is_valid(raise_exception=True)  # проверка данных на корректность в объекте сериализатора
        serializer.save()  # save() - вызовет update, если получает instance и data. Вызовет create, если на входе data.
        return Response({"post": serializer.data})  # ответ клиенту в виде JSON-строки об изменении данных

    def delete(self, request, *args, **kwargs):  # метод имеет свои аргументы, удаляющий запись по pk
        pk = kwargs.get("pk", None)  # получает ключ pk, иначе None
        if not pk:  # если нет, то вывод сообщения об ошибке
            return Response({"error": "Method DELETE not allowed"})

        # здесь нужна логика

        return Response({"post": "delete post " + str(pk)})  # вернуть ответ клиенту об удаленной записи


# class WomenAPIView(generics.ListAPIView):  # Базовый класс представления
#     queryset = Women.objects.all()  # взять все записи из таблицы Women
#     serializer_class = WomenSerializer  # класс сериализатора
