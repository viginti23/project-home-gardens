from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        null=True, blank=True,
        upload_to='account_pics/', default='default.png')


# class Profile:
#     pass
