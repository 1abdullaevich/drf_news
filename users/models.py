# user/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models
from main.models import *


class User(AbstractUser):
    username = models.CharField(max_length=55, unique=True)
    # Add related_name to avoid clashes with the default user model
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # You can use any custom name here
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',  # You can use any custom name here
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )

    def get_article_count(self):
        return self.articlemodel_set.count()
