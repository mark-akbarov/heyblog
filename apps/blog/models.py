from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from tinymce.models import HTMLField


class Blog(models.Model):
    title = models.CharField(max_length=150, )
    text = HTMLField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    class Meta:
        ordering = ('-date',)

    def count_posts_of(user):
        return Blog.objects.filter(author=user).count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'pk' : self.pk})


