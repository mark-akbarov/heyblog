from dataclasses import field
from django.db import models
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import (
    ListView, DetailView, 
    CreateView, UpdateView, 
    DeleteView)
from django.contrib.auth.mixins import (
LoginRequiredMixin, 
)

from blog.forms import BlogCommentForm
from .models import Blog, BlogComment



class BlogListView(ListView):
    model = Blog
    template_name = 'blog/home.html'
    object_list = 'blogs'
    ordering = ['-date']
    login_url = 'login'


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
    login_url = 'login'


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog 
    fields = ['title', 'text', 'image']
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = BlogComment
    template_name = 'blog/add_comment.html'
    form_class = BlogCommentForm
    success_url = reverse_lazy('blog/blog_detail.html')

    def form_valid(self, form):
        form.instance.blog = self.kwargs['pk']
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    template_name = 'blog/blog_update.html'
    fields = ['title', 'text']
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class BlogDeleteView(LoginRequiredMixin,  DeleteView):
    model = Blog
    template_name = 'blog/blog_delete_confirm.html'
    success_url = '/'
    login_url = 'login'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


