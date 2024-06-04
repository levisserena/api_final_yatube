"""URL для API."""
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet, PostFollowSet,
)

app_name = 'api'

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register('follow', FollowViewSet, basename='follow')
router.register('posts_following', PostFollowSet, basename='follow_post')
router.register(r'posts\/(?P<post_pk>\d+)\/comments',
                CommentViewSet,
                basename='comments')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
