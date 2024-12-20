# blog/forms.py
from django import forms
from .models import Post, Comment
from taggit.forms import TagField, TagWidget # type: ignore

class CustomUserCreationForm(UserCreationForm): # type: ignore
    email = forms.EmailField(required=True)

    class Meta:
        model = User # type: ignore
        fields = ['username', 'email', 'password1', 'password2']

class PostForm(forms.ModelForm):
    tags = TagField(widget=TagWidget)

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'tags': TagWidget(),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']