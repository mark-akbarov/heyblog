from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from comment.serializers import *
from comment.models import *


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def get_queryset(self):
        return Comment.objects.filter(blog_id=self.kwargs['blog_pk'])


class ReplyViewSet(ModelViewSet):
    serializer_class = ReplySerializer
    queryset = Reply.objects.all()

    def get_queryset(self):
        return Reply.objects.filter(post_id=self.kwargs['comment_pk'])

class ReplyListAPIView(ListAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer


class ReplyRetrieveAPIView(RetrieveAPIView):
    serializer_class = ReplySerializer
    queryset = Reply.objects.all()


