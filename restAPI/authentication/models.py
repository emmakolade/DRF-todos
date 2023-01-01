from django.db import models
from helpers.models import TrackingModel
from django.contrib.auth.models import PermissionsMixin, BaseUserManager, AbstractBaseUser
from django.contrib.auth.validators import UnicodeUsernameValidator


# Create your models here.

class User(TrackingModel, AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        _('user')
    )
    pass
