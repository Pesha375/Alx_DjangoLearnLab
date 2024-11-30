from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class CustomUser(AbstractUser):
    """
    Custom User Model extending Django's AbstractUser
    with additional fields: date_of_birth and profile_photo.
    """
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    def __str__(self):
        # Returning more detailed information for better representation in the admin
        return f"{self.username} ({self.first_name} {self.last_name})"


class Book(models.Model):
    """
    Book Model representing a book in the library system.
    Links to the custom user model via ForeignKey for user ownership.
    """
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.publication_year})"
