from rest_framework import serializers
from comment.models import Comment, Reply


class CommentSerializer(serializers.ModelSerializer):
    blog = serializers.StringRelatedField()
    author = serializers.StringRelatedField()
    class Meta:
        model = Comment
        fields = ['blog', 'author', 'body']


class ReplySerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    comment = serializers.StringRelatedField()
    class Meta:
        model = Reply
        fields = ['body', 'author', 'comment']