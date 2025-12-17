from django.contrib.auth.models import AbstractUser
from django.db import models


class Student(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True)

    def __str__(self) -> str:
        return f"{self.username} ({self.email})"

