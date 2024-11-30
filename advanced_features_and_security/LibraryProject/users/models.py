

# Create yourom django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager): # type: ignore
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser): # type: ignore
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    username = None  # Remove username field
    USERNAME_FIELD = 'email'  # Use email field for authentication
    REQUIRED_FIELDS = []  # Add fields required on create_superuser

    objects = CustomUserManager()

    class Meta:
        permissions = [
            ("can_view_user", "Can view user"),
            ("can_add_user", "Can add user"),
            ("can_change_user", "Can change user"),
            ("can_delete_user", "Can delete user"),
        ]

    def __str__(self):
        return self.email
