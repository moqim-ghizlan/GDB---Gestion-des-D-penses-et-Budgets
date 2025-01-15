from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    username = models.CharField(max_length=150, null=True, blank=True, unique=False)
    first_name = models.CharField(max_length=150, null=False)
    last_name = models.CharField(max_length=150, null=False)
    email = models.EmailField(max_length=254, null=False, unique=True)
    phone = models.CharField(max_length=150, null=True, blank=True)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

    def __str__(self):
        return f'{self.get_last_name()} {self.get_first_name()}'
    def get_last_name(self):
        return self.last_name.upper()
    def get_first_name(self):
        return self.first_name.title()
