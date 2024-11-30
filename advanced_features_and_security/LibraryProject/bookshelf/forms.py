from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year', 'isbn']
        labels = {
            'title': 'Book Title',
            'author': 'Author Name',
            'publication_year': 'Year of Publication',
            'isbn': 'ISBN Number',
        }
        help_texts = {
            'isbn': 'Enter a 13-character ISBN number.',
            'publication_year': 'Enter the year of publication (YYYY).',
        }
        widgets = {
            'publication_year': forms.NumberInput(attrs={'min': 1000, 'max': 9999}),
            'isbn': forms.TextInput(attrs={'maxlength': 13, 'placeholder': 'Enter ISBN number'}),
        }

    def clean_isbn(self):
        isbn = self.cleaned_data.get('isbn')
        if not isbn.isdigit():
            raise forms.ValidationError("ISBN must contain only digits.")
        if len(isbn) != 13:
            raise forms.ValidationError("ISBN must be exactly 13 digits long.")
        return isbn

    def clean_publication_year(self):
        year = self.cleaned_data.get('publication_year')
        if year < 1000 or year > 9999:
            raise forms.ValidationError("Please enter a valid year (YYYY).")
        return year
