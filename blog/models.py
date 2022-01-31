from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Blog(models.Model):
    title = models.CharField(max_length=150)
    text = models.CharField(max_length=280)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'pk' : self.pk})
