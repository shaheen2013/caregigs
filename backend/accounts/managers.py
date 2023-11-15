from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
        
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        if not password:
            raise ValueError("User must have a password")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.is_superuser = False
        user.is_staff = False
        user.save(using=self._db)
        return user
    

    def create_superuser(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        if not password:
            raise ValueError("User must have a password")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user
    

    def create_staffuser(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.is_superuser = False
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user
