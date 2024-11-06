from django.contrib import admin

# Register your models here.
from django.contrib import admin
from.models import Book
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Display fields in the admin list view
    list_display = ('title', 'author', 'publication_year')
    
    # Enable search by title and author
    search_fields = ('title', 'author')
    
    # Add filter options by publication year
    list_filter = ('publication_year',)





