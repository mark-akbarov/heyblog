from distutils.command import upload
from django.db import models
from django.urls import reverse
from users.models import Profile
from django.contrib.auth.models import User
from PIL import Image

class Blog(models.Model):
    title = models.CharField(max_length=150, default='Interesting Title')
    text = models.CharField(max_length=280, default='Text', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,)
    image = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'pk' : self.pk})


class Comment(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ('created',)
    
