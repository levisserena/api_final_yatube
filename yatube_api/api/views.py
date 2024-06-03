"""Представления приложения API."""
from django.shortcuts import get_object_or_404
from rest_framework.filters import SearchFilter
from rest_framework.permissions import (
    IsAuthenticated, IsAuthenticatedOrReadOnly)
from rest_framework.viewsets import ReadOnlyModelViewSet

from posts.models import Comment, Follow, Group, Post

from .mixin import VariablePaginatorMixin
from .permissions import IsAuthorOrReadOnly
from .serializers import (
    CommentSerializer, FollowSerializer, GroupSerializer, PostSerializer)


class PostViewSet(VariablePaginatorMixin):
    """Обрабатывает API запросы к моделе Post."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly,)

    def perform_create(self, serializer):
        """Метод сохраняет в БД запись.

        Здесь переопределен, чтобы поле "author" заполнялось автоматически.
        """
        serializer.save(author=self.request.user)


class GroupViewSet(ReadOnlyModelViewSet):
    """Обрабатывает API запросы к моделе Group."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(VariablePaginatorMixin):
    """Обрабатывает API запросы к моделе Comment."""

    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly,)

    def get_queryset(self):
        """Возвращает запрос к БД.

        Здесь переопределён, отсеиваются комментарии только определенного
        поста.
        """
        return Comment.objects.filter(post=self.get_post_id())

    def perform_create(self, serializer):
        """Метод сохраняет в БД запись.

        Здесь переопределен, чтобы поля "author" и "post" заполнялись
        автоматически.
        """
        post = get_object_or_404(Post, pk=self.get_post_id())
        serializer.save(author=self.request.user, post=post)

    def get_post_id(self):
        """Возвращает pk записи из запроса."""
        return self.kwargs.get('post_pk')


class FollowViewSet(VariablePaginatorMixin):
    """Обрабатывает систему подписки пользователя."""

    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (SearchFilter,)
    search_fields = ('^following__username',)

    def get_queryset(self):
        """Возвращает запрос к БД.

        Здесь переопределён, отсеиваются только подписки сделавшего запрос.
        """
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Метод сохраняет в БД запись.

        Здесь переопределен, чтобы поле "author" заполнялось автоматически.
        """
        serializer.save(user=self.request.user)
