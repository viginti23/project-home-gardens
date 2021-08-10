from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Zdjęcie profilowe:',
                              null=True, blank=True, 
                              default='account_pics/default.jpeg',
                              upload_to='account_pics/')

    def __str__(self):
        return f"Profil {self.user.username}"

    def get_absolute_url(self, *args, **kwargs):
        return reverse('account', kwargs={'pk': self.pk})
