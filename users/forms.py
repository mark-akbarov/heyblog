from django import forms
from django.contrib.auth.models import User
from .models import Profile


class RegisterForm(forms.Form):
    username = forms.CharField(label="Username",widget=forms.TextInput())
    name = forms.CharField(label="Name",widget=forms.TextInput())
    email = forms.EmailField(label="Email", widget=forms.TextInput())
    password_one = forms.CharField(label="Password", widget=forms.PasswordInput(render_value=False))
    password_two = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(render_value=False))


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

    
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']