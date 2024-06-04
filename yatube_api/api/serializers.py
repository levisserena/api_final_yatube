"""Сериализаторы."""
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import (
    CurrentUserDefault,
    ModelSerializer,
    PrimaryKeyRelatedField,
    SlugRelatedField,
)
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Group, Follow, Post, User


class AuthorMixinSerializer(ModelSerializer):
    """
    Миксин сериализатора на базе ModelSerializer.
    Добавляет поле author, подвязанное к модели User.
    """

    author = SlugRelatedField(slug_field='username', read_only=True)


class PostSerializer(AuthorMixinSerializer):
    """Сериализатор модели Post."""

    class Meta:
        """Методанные класса PostSerializer."""

        model = Post
        fields = ('id', 'text', 'group', 'pub_date', 'author', 'image')


class CommentSerializer(AuthorMixinSerializer):
    """Сериализатор модели Comment."""

    post = PrimaryKeyRelatedField(read_only=True)

    class Meta:
        """Методанные класса CommentSerializer."""

        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')


class GroupSerializer(ModelSerializer):
    """Сериализатор модели Group."""

    class Meta:
        """Методанные класса GroupSerializer."""

        model = Group
        fields = ('id', 'title', 'slug', 'description')


class FollowSerializer(ModelSerializer):
    """Сериализатор модели Follow."""

    user = SlugRelatedField(
        slug_field='username', read_only=True, default=CurrentUserDefault(),
    )
    following = SlugRelatedField(
        slug_field='username', queryset=User.objects.all(),
    )

    class Meta:
        """Методанные класса FollowSerializer."""
        model = Follow
        fields = ('user', 'following')
        read_only_fields = ('user',)
        validators = (
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following'),
                message='На этого пользователя Вы уже подписаны!'
            ),
        )

    def validate_following(self, following):
        """
        Валидирует поле following.
        Подписываться на самого себя нельзя.
        Если в POST запросе будет имя, совпавшее с именем пользователем,
        который отправил запрос, будет ошибка, и запись не создастся.
        """
        user = self.context['request'].user
        if user == following:
            raise ValidationError(detail='Подписаться на самого себя нельзя.')
        return following
