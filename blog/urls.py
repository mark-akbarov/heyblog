from django.urls import path
from .views import (BlogDetailView, 
BlogCreateView,  BlogUpdateView, BlogDeleteView, SubredditListView, TopBlogListView)
from . import views


urlpatterns = [
   path('', views.home, name='home'),
   path('top_posts/', TopBlogListView.as_view(), name='top_posts'),
   path('subreddit_posts/', SubredditListView.as_view(), name='subreddit_posts'),
   path('blog/new/', BlogCreateView.as_view(), name='blog_create'),
   path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
   path('blog/<int:pk>/update/', BlogUpdateView.as_view(), name='blog_update'),
   path('blog/<int:pk>/delete/', BlogDeleteView.as_view(), name='blog_delete'),


]