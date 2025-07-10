from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, ClassroomViewSet, ClassroomMemberViewSet,
    PostViewSet, CommentViewSet
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'classrooms', ClassroomViewSet)
router.register(r'classroom-members', ClassroomMemberViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]