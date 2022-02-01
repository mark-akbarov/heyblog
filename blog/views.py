from django.db import models
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import (
    ListView, DetailView, 
    CreateView, UpdateView, 
    DeleteView)
from django.contrib.auth.mixins import (
LoginRequiredMixin, UserPassesTestMixin 
)
from .models import Blog, BlogComment
from .forms import BlogCommentForm


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

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        comments_connected = BlogComment.objects.filter(blogpost_connected=self.get_object()).order_by('-date_posted')
        data['comments'] = comments_connected
        if self.request.user.is_authenticated:
            data['comment_form'] = BlogCommentForm(instance=self.request.user)

        return data

    def post(self, request, *args, **kwargs):
        new_comment = Blog(content=request.POST.get('content'), author=self.request.user, blogpost_connected=self.get_object())
        new_comment.save()
        return self.get(self, request, *args, **kwargs)


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog 
    fields = ['title', 'text', 'image']
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Blog
    template_name = 'blog/blog_update.html'
    fields = ['title', 'text']
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Blog
    template_name = 'blog/blog_delete_confirm.html'
    success_url = '/'
    login_url = 'login'


