"""Настройки зоны админа."""
from django.contrib import admin

from .models import Comment, Follow, Group, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Модель для администрирования постов."""

    list_display = ('pk', 'text', 'pub_date', 'author')
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Модель для администрирования комментариев."""

    list_display = ('pk', 'text', 'created', 'author', 'post')
    empty_value_display = '-пусто-'


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    """Модель для администрирования групп сообщества."""

    list_display = ('pk', 'slug', 'title',  'description')


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    """Модель для администрирования подписок."""

    list_display = ('pk', 'user', 'following')
