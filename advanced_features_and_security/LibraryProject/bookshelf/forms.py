from django import forms
from .models import Book

# Example of a form for creating a book
class ExampleForm(forms.Form):
    title = forms.CharField(max_length=100, label="Book Title")
    author = forms.CharField(max_length=100, label="Author Name")
    publication_date = forms.DateField(label="Publication Date", widget=forms.DateInput(attrs={'type': 'date'}))
    isbn = forms.CharField(max_length=13, label="ISBN", help_text="Enter the 13-character ISBN.")

    def clean_isbn(self):
        isbn = self.cleaned_data.get('isbn')
        if not isbn.isdigit():
            raise forms.ValidationError("ISBN must contain only digits.")
        if len(isbn) != 13:
            raise forms.ValidationError("ISBN must be exactly 13 characters long.")
        return isbn
