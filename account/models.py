from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
# Create your models here.
class User(AbstractUser):
    email = models.EmailField(
        max_length=150,
        unique= True
    )
    
    profile_picture = models.ImageField(
        blank=True,
        null=True,
        upload_to="user_profile"
    )
    
    REQUIRED_FIELDS = ["email"]
    objects = CustomUserManager()
    
    def __str__(self):
        return self.username