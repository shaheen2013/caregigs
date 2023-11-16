from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

# App imports
from .managers import UserManager


class BaseModel(models.Model):
    created_date = models.DateTimeField(default=timezone.now, editable=False)
    updated_date = models.DateTimeField(auto_now=True, editable=False, null=True)

    class Meta:
        abstract = True


class CustomUser(AbstractUser, BaseModel):
    username = models.CharField(max_length=128, null=True, unique=False, blank=True)
    email = models.EmailField(unique=True, blank=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        ordering = ("first_name",)

