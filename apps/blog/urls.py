from atexit import register
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog.views import *

router = DefaultRouter()
router.register('blog', BlogViewSet)

urlpatterns = [
   path('', include(router.urls))
]
