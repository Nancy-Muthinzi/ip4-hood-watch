from django import forms
from .models import Post, Business
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['title'] 

class NewBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['profile']           
