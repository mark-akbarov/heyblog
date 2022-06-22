from django import template
from django.db.models import Count
from blog.models import Blog

register = template.Library()

@register.simple_tag
def get_most_commented_posts(count=5):
    return Blog.objects.annotate( total_comments=Count('comments')).order_by('-total_comments')[:count]


@register.simple_tag
def get_all_commented_posts(count=10):
    return Blog.objects.annotate( total_comments=Count('comments')).order_by('-total_comments')[:count]
