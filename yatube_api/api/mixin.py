"""Миксины для views.py."""
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import GenericViewSet


class VariablePaginatorMixin(GenericViewSet):
    """Миксин для добавления вариативного пагинатора."""

    @property
    def paginator(self):
        """
        Переопределённый метод выбора пагинатора.
        Если запрос содержит параметр 'limit' воспользуется пагинатором.
        В противном случае разбивки по страницам не будет.
        """
        if not hasattr(self, '_paginator'):
            if 'limit' in self.request.query_params:
                self.pagination_class = LimitOffsetPagination
                self._paginator = self.pagination_class()
            else:
                self._paginator = None
        return self._paginator
