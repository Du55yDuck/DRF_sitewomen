import io

from rest_framework import serializers  # импорт сериализатора
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Women  # импорт модели Women


# class WomenModel:  # класс, объекты которого будут сериализоваться (перевод в JSON-строку)
#     def __init__(self, title, content):  # передача локальных атрибутов
#         self.title = title  # имена переменных должны совпадать с именами в модели-сериализ-ре (class WomenSerializer)
#         self.content = content


class WomenSerializer(serializers.ModelSerializer):  # класс, сериализует объекты Women (наследуем от ModelSerializer)
    class Meta:  # вложенный класс для работы с моделью Women
        model = Women  # указана модель
        fields = "__all__"  # все поля из бд возвращаемые клиенту (можно указать конкретные "title", "content", ...)

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


