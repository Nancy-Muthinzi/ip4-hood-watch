from django import forms
from .models import Post, Business, Hood
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post']
        

class NewBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['profile']           

class NewHoodForm(forms.ModelForm):
    class Meta:
        model = Hood
        exclude = ['profile']  