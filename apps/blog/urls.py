from django.urls import path
from .views import (BlogDetailView, BlogCreateView,  
BlogUpdateView, BlogDeleteView, TopBlogListView)
from . import views


urlpatterns = [
   path('', views.home, name='home'),
   path('top_posts/', TopBlogListView.as_view(), name='top_posts'),
   path('new/', BlogCreateView.as_view(), name='blog_create'),
   path('<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
   path('<int:pk>/update/', BlogUpdateView.as_view(), name='blog_update'),
   path('<int:pk>/delete/', BlogDeleteView.as_view(), name='blog_delete'),
]