from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from tinymce.models import HTMLField
from PIL import Image


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
    blogpost_connected = models.ForeignKey( Blog, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)


    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'pk' : self.pk})

    def children(self):
        return str(self.user.username)

    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True

    def __str__(self):
        return str(self.author) + ', ' + self.blogpost_connected.title[:40] 


class SubReddit(models.Model):
    name = models.CharField(max_length=200)
    posts = models.ManyToManyField(Blog, related_name='subreddits', blank=True, through='SubRedditPost')
    image = models.ImageField(blank=True, null=True, default='default.jpg' )
    moderators = models.ManyToManyField(User, related_name='subreddits_moderated')
    objects = models.Manager()

    def save(self, *args, **kwargs):
        super(SubReddit, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
 
    def __str__(self):
        return self.name
 
class SubRedditPost(models.Model):
    subreddit = models.ForeignKey(SubReddit, related_name='posts_set', on_delete=models.CASCADE)
    post = models.ForeignKey(Blog, related_name='subreddits_set', on_delete=models.CASCADE)
 
    class Meta: unique_together = ['subreddit', 'post']
 