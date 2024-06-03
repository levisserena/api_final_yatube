"""Настройка разрешений."""
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorOrReadOnly(BasePermission):
    """Разрешение на уровне объекта.

    Разрешает редактировать объект только его владельцам.
    Предполагается, что экземпляр модели имеет атрибут `author`.
    """

    message = 'Изменять чужие записи у нас не принято.'

    def has_object_permission(self, request, view, obj):
        """Метод класса IsAuthorOrReadOnly.

        Проверка на уровне объекта. Вернет True если проверка пройдена,
        и False - если нет.
        """
        return request.method in SAFE_METHODS or (
            obj.author == request.user
        )
