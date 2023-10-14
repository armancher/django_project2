import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    personnel_number = models.UUIDField(default=uuid.uuid4)
    phone_number = models.CharField(max_length=11, blank=True)

    def __str__(self):
        return self.username

