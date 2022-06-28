from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from blog.models import Blog

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body = HTMLField()

    def __str__(self) -> str:
        return f'Comment by {self.author} on {self.blog}'


class Reply(models.Model):
    comment = models.ForeignKey(Comment, related_name='replies', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = HTMLField()

    class Meta:
        verbose_name_plural = 'replies'

    def __str__(self) -> str:
        return self.author.username
    
    @property
    def get_replies(self):
        return self.replies.all()
