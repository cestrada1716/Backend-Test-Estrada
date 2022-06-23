# import python modules
import uuid

# import django configs
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.db import models

# import constants from this app
from .constants import USER_ROLES


class UserCornershop(AbstractBaseUser, PermissionsMixin, models.Model):

    objects = UserManager()
    id = models.UUIDField(
        primary_key=True, unique=True, default=uuid.uuid4, editable=False
    )
    full_name = models.CharField(max_length=200)
    slack_id = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=10)
    user_type = models.CharField(max_length=10, choices=USER_ROLES, default="employee")
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=500)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = "username"
