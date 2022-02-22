from rest_framework import generics
from .serializers import BlogSerializer
from blog import models


class BlogListAPIView(generics.ListCreateAPIView):
    queryset = models.Blog.objects.all()
    serializer_class = BlogSerializer


class BlogDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Blog.objects.all()
    serializer_class = BlogSerializer
