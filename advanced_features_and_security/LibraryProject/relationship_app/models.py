from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


# Author Model
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Book Model
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)

    class Meta:
        permissions = [
            ("can_view_book", "Can view book"),
            ("can_create_book", "Can create book"),
            ("can_edit_book", "Can edit book"),
            ("can_delete_book", "Can delete book"),
        ]

    def __str__(self):
        return self.title


# Library Model
class Library(models.Model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book, related_name='libraries')

    class Meta:
        permissions = [
            ("can_view_library", "Can view library"),
            ("can_create_library", "Can create library"),
            ("can_edit_library", "Can edit library"),
            ("can_delete_library", "Can delete library"),
        ]

    def __str__(self):
        return self.name


# Librarian Model
class Librarian(models.Model):
    name = models.CharField(max_length=255)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarian')

    class Meta:
        permissions = [
            ("can_view_librarian", "Can view librarian"),
            ("can_create_librarian", "Can create librarian"),
            ("can_edit_librarian", "Can edit librarian"),
            ("can_delete_librarian", "Can delete librarian"),
        ]

    def __str__(self):
        return self.name


# UserProfile Model
class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Member')

    class Meta:
        permissions = [
            ("can_view_user_profile", "Can view user profile"),
            ("can_create_user_profile", "Can create user profile"),
            ("can_edit_user_profile", "Can edit user profile"),
            ("can_delete_user_profile", "Can delete user profile"),
        ]

    def __str__(self):
        return f"{self.user.username} - {self.role}"


# Automatically create or update UserProfile when a User is created or updated
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        if hasattr(instance, 'userprofile'):
            instance.userprofile.save()
