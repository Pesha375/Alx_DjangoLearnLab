from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'  # Ensure all fields are part of the form
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
            'title': forms.TextInput(attrs={'maxlength': 255, 'placeholder': 'Enter Book Title'}),
            'author': forms.TextInput(attrs={'maxlength': 255, 'placeholder': 'Enter Author Name'}),
        }

    def clean_isbn(self):
        isbn = self.cleaned_data.get('isbn')
        
        # Validate that the ISBN contains only digits and is 13 characters long
        if not isbn.isdigit():
            raise forms.ValidationError("ISBN must contain only digits.")
        if len(isbn) != 13:
            raise forms.ValidationError("ISBN must be exactly 13 characters long.")
        return isbn

    def clean_title(self):
        title = self.cleaned_data.get('title')
        # Sanitize the title to avoid dangerous input (e.g., XSS)
        if '<' in title or '>' in title:
            raise forms.ValidationError("Book title cannot contain angle brackets.")
        return title

    def clean_author(self):
        author = self.cleaned_data.get('author')
        # Sanitize the author field to prevent XSS issues
        if '<' in author or '>' in author:
            raise forms.ValidationError("Author name cannot contain angle brackets.")
        return author

    def clean_publication_date(self):
        publication_date = self.cleaned_data.get('publication_date')
        # Ensure that the publication date is in the correct format and valid
        if not publication_date:
            raise forms.ValidationError("Please enter a valid publication date.")
        return publication_date
