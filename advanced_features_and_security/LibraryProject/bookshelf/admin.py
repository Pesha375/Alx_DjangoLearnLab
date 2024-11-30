from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, UserProfile, Book, Author, Library, Librarian  # Import necessary models


# Register the CustomUser model in the admin panel using admin.site.register
class CustomUserAdmin(UserAdmin):
    """
    Custom configuration for the CustomUser model in the admin.
    """
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'date_of_birth', 'profile_photo', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'date_of_birth')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),  # Default username and password fields
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'date_of_birth', 'profile_photo')}),  # Personal fields
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),  # Permissions fields
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),  # Date fields
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'date_of_birth', 'profile_photo'),
        }),
    )
    ordering = ('username',)


# Register CustomUserAdmin with admin.site.register
admin.site.register(CustomUser, CustomUserAdmin)


# Register UserProfile model
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """
    Admin configuration for the UserProfile model.
    """
    list_display = ('user', 'role')
    search_fields = ('user__username', 'role')
    list_filter = ('role',)


# Register the Book model
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Book model.
    """
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)


# Register the Author model
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Author model.
    """
    list_display = ('name',)
    search_fields = ('name',)


# Register the Library model
@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Library model.
    """
    list_display = ('name',)
    search_fields = ('name',)


# Register the Librarian model
@admin.register(Librarian)
class LibrarianAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Librarian model.
    """
    list_display = ('name', 'library')
    search_fields = ('name', 'library__name')






            
