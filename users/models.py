from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField


class Account(models.Model):
    profile_image = models.ImageField(verbose_name='Zdjęcie profilowe:    ',
                                      null=True, blank=True,
                                      default='account_pics/kaktus.jpg',
                                      upload_to='account_pics/')

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Użytkownik:')
    phone_number = PhoneNumberField(blank=True, null=True, region='PL', verbose_name='Numer telefonu:')
    description = models.TextField(max_length=512, blank=True, null=True, verbose_name="Krótki opis:")
    location = models.CharField(max_length=64, blank=True, null=True, verbose_name='Napisz skąd jesteś:')

    def __str__(self):
        return f"Profil {self.user.username}"

    def get_absolute_url(self, *args, **kwargs):
        return reverse('account', kwargs={'pk': self.pk})
