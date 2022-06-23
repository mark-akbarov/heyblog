from django.shortcuts import render
from django.views.generic import (
    ListView, DetailView, 
    CreateView, UpdateView, 
    DeleteView)
from django.contrib.auth.mixins import (
LoginRequiredMixin, 
)
from django.db.models import Q
from .models import Blog


def home(request):
    blogs = Blog.objects.all()
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    posts_filter = Blog.objects.filter(Q(title__icontains=q))
    context = {'blogs': blogs, 'posts_filter': posts_filter}
    return render(request, 'blog/home.html', context)


class TopBlogListView(ListView):
    model = Blog
    template_name = 'blog/top_posts.html'


class UserPostListView(ListView):
    model = Blog
    template_name = 'user/profile.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

    def count_posts_of(user):
        return Blog.objects.filter(author=user).count()


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
    login_url = 'login'

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog 
    fields = ['title', 'text', 'image', 'status']
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
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


