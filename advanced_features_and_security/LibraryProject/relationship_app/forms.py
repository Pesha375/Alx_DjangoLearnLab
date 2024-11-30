from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        labels = {
            'title': 'Book Title',
            'author': 'Author Name',
            'publication_date': 'Date of Publication',
            'isbn': 'ISBN Number',
        }
        help_texts = {
            'isbn': 'Enter the 13-character ISBN.',
            'publication_date': 'Format: YYYY-MM-DD.',
        }
        widgets = {
            'publication_date': forms.DateInput(attrs={'type': 'date'}),
            'isbn': forms.TextInput(attrs={'maxlength': 13, 'placeholder': 'Enter ISBN'}),
        }

    def clean_isbn(self):
        isbn = self.cleaned_data.get('isbn')
        if not isbn.isdigit():
            raise forms.ValidationError("ISBN must contain only digits.")
        if len(isbn) != 13:
            raise forms.ValidationError("ISBN must be exactly 13 characters long.")
        return isbn
