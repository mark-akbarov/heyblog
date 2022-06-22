from django.urls import path
from . import views
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('logout/', auth_view.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('login/', auth_view.LoginView.as_view(template_name='user/login.html'), name='login'),
]