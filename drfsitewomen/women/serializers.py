from rest_framework import serializers  # импорт сериализатора
from .models import Women  # импорт модели Women


class WomenSerializer(serializers.ModelSerializer):  # класс, сериализует объекты Women (наследуем от ModelSerializer)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault)  # скрыв-т и связ поле user с текущ польз-ем

    class Meta:  # вложенный класс для работы с моделью Women
        model = Women  # указана модель
        fields = "__all__"  # все поля из бд возвращаемые клиенту (можно указать конкретные "title", "content", ...)
