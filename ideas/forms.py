from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Idea, Comment

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = ['category', 'title', 'description', 'image_url', 'company_name', 'location', 'application_url']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'category': forms.Select(choices=Idea.CATEGORY_CHOICES)
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3})
        }