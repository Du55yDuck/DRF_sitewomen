from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):  # custom permission - чтение всем и удаление админам
    def has_permission(self, request, view):  # ограничение доступа на уровне всего запроса
        if request.method in permissions.SAFE_METHODS:  # проверка метода на безопасность, only read(GET, HEAD, OPTIONS)
            return True  # права доступа всем

        return bool(request.user and request.user.is_staff)  # иначе доступ дается только админу


class IsOwnerOrReadOnly(permissions.BasePermission):  # custom permission - чтение всем и изменять авторам
    def has_object_permission(self, request, view, obj):  # ограничения на уровне объекта(записи) в запросе
        if request.method in permissions.SAFE_METHODS:  # проверка на безопасность
            return True  # если да - доступ чтение всем

        return obj.user == request.user  # user из бд == user из запроса - доступ разрешен автору
