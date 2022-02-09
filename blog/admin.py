from django.contrib import admin
from .models import Blog, BlogComment, SubReddit, SubRedditPost

admin.site.register(Blog)
admin.site.register(BlogComment)
admin.site.register(SubReddit)
admin.site.register(SubRedditPost)
