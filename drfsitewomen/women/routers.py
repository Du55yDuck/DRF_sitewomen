from rest_framework import routers


class MyCustomRouter(routers.SimpleRouter):  # пример пользовательского роутера (без / в конце)
    routes = [  # Класс взят из документации. Routes - список наших маршрутов
        routers.Route(url=r'^{prefix}$',  # Первый шаблон маршрута читает список статей (регулярное выражение)
                      mapping={'get': 'list'},  # связывает тип запроса с соответствующим методом ViewSet-а
                      name='{basename}-list',  # название маршрута
                      detail=False,  # список или отдельная запись
                      initkwargs={'suffix': 'List'}),  # доп аргументы передаются при определении маршрута
        routers.Route(url=r'^{prefix}/{lookup}$',  # Шаблон второго маршрута - читает конкретную статью по ее pk
                      mapping={'get': 'retrieve'},
                      name='{basename}-detail',
                      detail=True,
                      initkwargs={'suffix': 'Detail'})
    ]
