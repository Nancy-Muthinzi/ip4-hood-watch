from django import forms
from .models import Post
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        # model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        fields = ('first_name', 'last_name', 'email')

class PostForm(forms.Form):
    class Meta:
        # model = Post
        fields = ['post']
