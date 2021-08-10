from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
# from django.conf import settings

# fs = FileSystemStorage(location=settings.MEDIA_ROOT)
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=25, blank=True, null=True)

    
class Offer(models.Model):

    title = models.CharField(
        max_length=100, verbose_name="Nazwa przedmiotu:", null=True, blank=True)
    description = models.TextField(
        max_length=500, verbose_name="Opis:", null=True, blank=True)
    price = models.FloatField(verbose_name="Cena:", null=True, blank=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Sprzedawca: ')
    date_posted = models.DateTimeField(default=timezone.now)
    negotiable = models.BooleanField(verbose_name='Do negocjacji', default=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, default=None, verbose_name='Kategoria', null=True, blank=True)
    # location = models.TextField()

    def __str__(self):  
        return f'{self.title}'


    def get_absolute_url(self, *args, **kwargs):
        return reverse('offerdetail', kwargs={'pk': self.pk})
    
class OfferImage(models.Model):
    image = models.ImageField(verbose_name="  ",
        null=True, blank=True, 
        upload_to='products_pics/', default='products_pics/default.png')

    offer = models.ForeignKey(
        Offer, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.offer.title} - Photo'


