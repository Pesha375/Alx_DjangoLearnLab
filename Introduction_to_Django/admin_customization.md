# Admin Customization

To customize the admin interface for the Book model, modify `bookshelf/admin.py` to include the following code:
```python
from django.contrib import admin
from.models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author')

admin.site.register(Book, BookAdmin)