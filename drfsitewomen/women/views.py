from django.forms import model_to_dict  # импорт спец функции, преобразовывает объект в словарь
from django.shortcuts import render
from rest_framework import generics, viewsets  # импорт generics
from rest_framework.decorators import action  # импорт action
from rest_framework.response import Response  # импорт response
from rest_framework.views import APIView  # импорт базового класса APIView

from .models import Women, Category  # модель Women, также имя модели берется в каждый URL[name='women-list']
from .serializers import WomenSerializer


class WomenViewSet(viewsets.ModelViewSet):  # Класс от ModelViewSet для CRUD
    # queryset = Women.objects.all()  # Если queryset не указан, то необходимо добавить basename в роутер.
    serializer_class = WomenSerializer

    def get_queryset(self):  # переопределенный метод для вывода не всех записей, а только первые 3 при запросах
        pk = self.kwargs.get("pk")  # получить ключ pk

        if not pk:  # проверка на наличие pk(если есть women/1, то вернуть одну запись по pk в виде списка!)
            return Women.objects.all()[:3]  # вернуть 3 первые записи

        return Women.objects.filter(pk=pk)  # filter возвращает список, по скольку queryset должен вернуть список

    @action(methods=['get'], detail=True)  # GET считывает список категорий, detail=False возвращает список, вместо 1-й
    def category(self, request, pk=None):  # обязательные параметры (pk - дает возможность выбора отдельной категории)
        cats = Category.objects.get(pk=pk)  # прочесть категорию из модели Category по ключу pk (../women/1/category)
        return Response({'cats': cats.name})  # вернуть JSON ответ в виде словаря (категория: название)


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

