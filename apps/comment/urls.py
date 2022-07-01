from django.urls import path
from rest_framework_nested.routers import NestedDefaultRouter, DefaultRouter
from comment.views import *

urlpatterns = [
    path('blogs/<blog_id>/comments/<comment_id>/replies/', ReplyListAPIView.as_view()),
    path('blogs/<blog_pk>/comments/<comment_pk>/replies/<pk>', ReplyRetrieveAPIView.as_view()),
]
