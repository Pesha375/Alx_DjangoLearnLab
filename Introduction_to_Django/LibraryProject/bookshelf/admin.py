from django.contrib import admin

# Register your models here.
# bookshelf/admin.py
from django.contrib import admin
from .models import Book  # Import the Book model

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Fields to display in the list view
    search_fields = ('title', 'author')  # Enable search by title and author
    list_filter = ('publication_year',)  # Add filter by publication year


'bookshelf',


            
