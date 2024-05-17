import io

from rest_framework import serializers  # импорт сериализатора
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Women  # импорт модели Women


# class WomenModel:  # класс, объекты которого будут сериализоваться (перевод в JSON-строку)
#     def __init__(self, title, content):  # передача локальных атрибутов
#         self.title = title  # имена переменных должны совпадать с именами в модели-сериализ-ре (class WomenSerializer)
#         self.content = content


class WomenSerializer(serializers.Serializer):  # класс, сериализует объекты WomenModel (наследуем от serializer)
    title = serializers.CharField(max_length=255)  # поле Заголовок с валидатором CharField и ограничением 255 символов
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)  # Дата и время создания (только чтение)
    time_update = serializers.DateTimeField(read_only=True)  # Дата и время изменения
    is_published = serializers.BooleanField(default=True)  # статус публикации - по умолчанию включен
    cat_id = serializers.IntegerField()  # категория как int из-за подачи в JSON-строках

    def create(self, validated_data):  # стандартный метод сериализатора создания новых данных в бд
        return Women.objects.create(**validated_data)  # через Women создать (распакованный словарь validated_data)

    def update(self, instance, validated_data):  # метод для обновления данных сериализатором
        instance.title = validated_data.get("title", instance.title)  # instance - ссылка на объект Women (взять нужный
        instance.content = validated_data.get("content", instance.content)  # key из словаря, иначе вернуть key из Women
        instance.time_update = validated_data.get("time_update", instance.time_update)  # обновить время
        instance.is_published = validated_data.get("is_published", instance.is_published)
        instance.cat_id = validated_data.get("cat_id", instance.cat_id)
        instance.save()
        return instance  # вернуть instance


# def encode():  # ф-я для примера (преобразование объектов WomenModel в JSON)
#     model = WomenModel('Angelina Jolie', 'Content: Angelina Jolie')  # модель объекта WomenModel
#     model_sr = WomenSerializer(model)  # результат сериализации в виде объекта, а не JSON
#     print(model_sr.data, type(model_sr.data), sep='\n')  # вывод в консоль для проверки(data - сериализованные данные)
#     json = JSONRenderer().render(model_sr.data)  # перевод model_sr в формат JSON-строки через JsonRenderer()
#     print(json)  # вывод результата


# def decode():  # ф-я делает обратное encode() - преобразует из байтового JSON в обычный словарь.
#     stream = io.BytesIO(b'{"title":"Angelina Jolie","content":"Content: Angelina Jolie"}')  # имитация входного потока
#     data = JSONParser().parse(stream)  # словарь в которой помещается распарсерные данные (от класса JSONParser.parse)
#     serializer = WomenSerializer(data=data)  # получение объекта сериализации с именованным параметром data (декодинг)
#     serializer.is_valid()  # проверка на корректность
#     print(serializer.validated_data)  # вывод корректных сериализованных данных (результат декодирования JSON-строки)


