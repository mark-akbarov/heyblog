from distutils.command import upload
from django.db import models
from django.urls import reverse
from django.utils import timezone
from users.models import Profile
from django.contrib.auth.models import User
from PIL import Image

class Blog(models.Model):
    title = models.CharField(max_length=150, default='Interesting Title')
    text = models.CharField(max_length=280, default='Text', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,)
    image = models.ImageField(null=True, blank=True, upload_to='images/')

    @property
    def number_of_comments(self):
        return Comment.objects.filter(blogpost_connected=self).count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'pk' : self.pk})


class Comment(models.Model):
    blogpost_connected = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE, default='Comment')
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.author) + ', ' + self.blogpost_connected.title[:40]
