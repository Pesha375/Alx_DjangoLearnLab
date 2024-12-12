from .models import Post, Comment

# blog/forms.py
from django import forms
from .models import Post, Tag

class CustomUserCreationForm(UserCreationForm): # type: ignore
    email = forms.EmailField(required=True)

    class Meta:
        model = User # type: ignore
        fields = ['username', 'email', 'password1', 'password2']

class PostForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']