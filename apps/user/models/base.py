from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    MODERATOR = 'moderator'
    USER = 'user'
    TYPES = (
        (MODERATOR, MODERATOR),
        (USER, USER)
    )
    user_type = models.CharField(max_length=20, choices=TYPES)