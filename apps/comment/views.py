from rest_framework.viewsets import ModelViewSet
from comment.serializers import *
from comment.models import *


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(blog_id=self.kwargs['blog_pk'])


class ReplyViewSet(ModelViewSet):
    serializer_class = ReplySerializer

    def get_queryset(self):
        return Reply.objects.filter(post_id=self.kwargs['comment_pk'])