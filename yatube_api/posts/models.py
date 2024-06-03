"""Модели проекта."""
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models

User = get_user_model()


class Group(models.Model):
    """Модель групп постов."""

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        """Метод отвечающий за строковое представление объекта."""
        return self.title


class Post(models.Model):
    """Модель постов."""

    text = models.TextField()
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор',
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name='posts',
        blank=True,
        null=True,
        verbose_name='Группа',
    )
    image = models.ImageField(
        upload_to='image/posts/',
        null=True, blank=True,
        verbose_name='Картинка',
    )

    def __str__(self):
        """Метод отвечающий за строковое представление объекта."""
        return self.text


class Comment(models.Model):
    """Модель коментариев."""

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор',
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Пост',
    )
    text = models.TextField(verbose_name='Текст')
    created = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name='Дата создания',
    )

    def __str__(self):
        """Метод отвечающий за строковое представление объекта."""
        return self.text


class Follow(models.Model):
    """Модель для подписки на других пользователей."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='fan',
        verbose_name='Фанатик',
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Айдол',
    )

    class Meta:
        """Методанные модели Follow."""

        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'],
                name='unique_user_following'
            )
        ]

    def __str__(self):
        """Метод отвечающий за строковое представление объекта."""
        return f'{self.user} подписан на {self.following}'

    def clean(self):
        """Метод не допустит подписатся на самого себя."""
        if self.user == self.following:
            raise ValidationError(
                'Подписываться самому на себя нельзя!'
            )
