from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from tinymce.models import HTMLField


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset() \
                                            . filter(status='published')

class Blog(models.Model):

    STATUS_CHOICES = ( ('draft', 'Draft'), ('published', 'Published'),)

    title = models.CharField(max_length=150, )
    text = HTMLField(default='', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    tags = TaggableManager()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ('-date',)

    @property
    def number_of_comments(self):
        return BlogComment.objects.filter(blogpost_connected=self).count()
   
    def count_posts_of(user):
        return Blog.objects.filter(author=user).count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'pk' : self.pk})


class BlogComment(models.Model):
    blogpost_connected = models.ForeignKey(
        Blog, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.author) + ', ' + self.blogpost_connected.title[:40] 