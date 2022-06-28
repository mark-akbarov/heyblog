from rest_framework_nested.routers import DefaultRouter, NestedDefaultRouter
from blog.views import *
from comment.views import *

router = DefaultRouter()
router.register('blogs', BlogViewSet)

posts_router = NestedDefaultRouter(router, 'blogs', lookup='blog')
posts_router.register('comments', CommentViewSet, basename='blog-comments')
posts_router.register('reviews', ReplyViewSet, basename='blog-reviews')


urlpatterns = router.urls + posts_router.urls