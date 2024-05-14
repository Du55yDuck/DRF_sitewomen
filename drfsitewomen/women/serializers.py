from rest_framework import serializers  # импорт сериализатора
from .models import Women  # импорт модели Women


class WomenSerializer(serializers.ModelSerializer):  # класс сериализатора, работающего с моделями из бд.
    class Meta:
        model = Women  # модель Women
        fields = ('title', 'cat_id')  # поля для сериализации (отправляются обратно пользователю)
