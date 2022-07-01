from django.urls import path
from rest_framework_nested.routers import DefaultRouter, NestedDefaultRouter
from blog.views import *
from comment.views import *

router = DefaultRouter()
router.register('blogs', BlogViewSet)

blogs_router = NestedDefaultRouter(router, 'blogs', lookup='blog')
blogs_router.register('comments', CommentViewSet, basename='blog-comments')

urlpatterns = router.urls + blogs_router.urls