from django import forms
from .models import Book # type: ignore

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'  # Or specify fields like ['field1', 'field2']
