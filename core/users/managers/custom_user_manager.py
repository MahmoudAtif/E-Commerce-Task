from django.contrib.auth.models import UserManager


class CustomUserManager(UserManager):
    
    def _create_user(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError("User must have an email address")
        
        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,  
            **extra_fields       
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, username, email, password, **extra_fields):
        extra_fields.set_default('is_staff', False)
        extra_fields.set_default('is_superuser', False)
        return self._create_user(
            username,
            email,
            password,
            **extra_fields
        )
    
    def create_superuser(self, username, email, password, **extra_fields):        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self._create_user(
            username, 
            email, 
            password, 
            **extra_fields
        )
        