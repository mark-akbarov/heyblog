from django.db import models
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import (
    ListView, DetailView, 
    CreateView, UpdateView, 
    DeleteView)
from .models import Blog


def home(request):
    context = {
        'blogs': Blog.objects.all()
    }
    return render(request, 'blogs/home.html', context)


class BlogListView(ListView):
    model = Blog
    template_name = 'blog/home.html'
    object_list = 'blogs'
    ordering = ['-date']


class BlogDetailView(DetailView):
    model = Blog


class BlogCreateView(CreateView):
    model = Blog 
    template_name = 'blog/blog_create.html'
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['title', 'body']
    template_name = 'blog/blog_update.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = '/'
    template_name = 'blog/blog_delete_confirm.html'


