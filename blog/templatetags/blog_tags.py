from django import template
from blog.models import Blog
from django.db.models import Count


register = template.Library()


@register.simple_tag
def get_most_commented_posts(count=5):
    return Blog.published.annotate( total_comments=Count('comments')).order_by('-total_comments')[:count]


@register.simple_tag
def get_all_commented_posts(count=10):
    return Blog.published.annotate( total_comments=Count('comments')).order_by('-total_comments')[:count]
