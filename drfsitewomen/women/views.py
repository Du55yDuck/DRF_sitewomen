from rest_framework import viewsets, generics  # импорт generics
from rest_framework.decorators import action  # импорт action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response  # импорт response

from .models import Women, Category  # модель Women, также имя модели берется в каждый URL[name='women-list']
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import WomenSerializer


# class WomenViewSet(viewsets.ModelViewSet):  # Класс от ModelViewSet для CRUD
#     # queryset = Women.objects.all()  # Если queryset не указан, то необходимо добавить basename в роутер.
#     serializer_class = WomenSerializer
#
#     def get_queryset(self):  # переопределенный метод для вывода не всех записей, а только первые 3 при запросах
#         pk = self.kwargs.get("pk")  # получить ключ pk
#
#         if not pk:  # проверка на наличие pk(если есть women/1, то вернуть одну запись по pk в виде списка!)
#             return Women.objects.all()[:3]  # вернуть 3 первые записи
#
#         return Women.objects.filter(pk=pk)  # filter возвращает список, по скольку queryset должен вернуть список
#
#     @action(methods=['get'], detail=True)  # GET считывает список категорий, detail=False возвращае список, вместо 1-й
#     def category(self, request, pk=None):  # обязательные параметры (pk - дает возможность выбора отдельной категории)
#         cats = Category.objects.get(pk=pk)  # прочесть категорию из модели Category по ключу pk (../women/1/category)
#         return Response({'cats': cats.name})  # вернуть JSON ответ в виде словаря (категория: название)


class WomenAPIList(generics.ListCreateAPIView):  # ListCreateAPIView - чтение данных (GET)
    queryset = Women.objects.all()  # атрибут ссылается на список записей, возвращаемый клиенту
    serializer_class = WomenSerializer  # сериализатор применяется к queryset
    # permission_classes = (IsAuthenticatedOrReadOnly, )  # чтение всем или изменение для авторизованных (tuple or list)


class WomenAPIUpdate(generics.RetrieveUpdateAPIView):  # Изменение автору, чтение всем (PUT, PATCH-запросы)
    queryset = Women.objects.all()  # Клиенту возвращаются не все записи, а только измененные (ленивый запрос)
    serializer_class = WomenSerializer
    permission_classes = (IsOwnerOrReadOnly, )  # чтение для всех, изменение статей авторам (class custom permission)


class WomenAPIDestroy(generics.RetrieveDestroyAPIView):  # удаляет данных (DELETE-запросы)
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAdminOrReadOnly, )  # удаления только для админов, чтение для всех (class custom permission)
