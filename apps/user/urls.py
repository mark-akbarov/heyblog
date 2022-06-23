from django.contrib.auth import views as auth_view
from django.urls import path
from .forms import LoginForm
from . import views

app_name = 'user'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login, name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
]