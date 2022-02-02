from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

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
