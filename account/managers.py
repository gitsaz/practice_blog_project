from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError("email must be set")
        if not password:
            raise ValueError("password must be set")
        
        user = self.model(
            username=username,
            email=email,
            password=password,
            **extra_fields
        )
        user.set_password(password)
        user.save()
    
    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('is_staff must be true')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('is_superuser must be true')
        
        return self.create_user(
            
            username=username,
            email=email,
            password=password,
            **extra_fields
        )