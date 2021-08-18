from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.core.files.storage import FileSystemStorage

# from django.conf import settings

# fs = FileSystemStorage(location=settings.MEDIA_ROOT)
# Create your models here.


class SizeCategory(models.Model):
    name = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        verbose_name_plural = "size categories"

    def __str__(self):
        return f'{self.name}'


class MaintenanceCategory(models.Model):
    name = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        verbose_name_plural = "maintenance categories"

    def __str__(self):
        return f'{self.name}'


class Offer(models.Model):
    title = models.CharField(
        max_length=100, verbose_name="Nazwa przedmiotu:", null=True, blank=True)
    description = models.TextField(
        max_length=1024, verbose_name="Opis:", null=True, blank=True)
    price = models.FloatField(verbose_name="Cena:", null=True, blank=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Sprzedawca: ')
    date_posted = models.DateTimeField(default=timezone.now)
    negotiable = models.BooleanField(verbose_name='Do negocjacji', default=True)
    size_category = models.ForeignKey(SizeCategory, on_delete=models.DO_NOTHING,
                                      default=None, verbose_name='Wielkość rośliny', null=True, blank=True)
    maintenance_category = models.ForeignKey(MaintenanceCategory,
                                             on_delete=models.DO_NOTHING, default=None,
                                             verbose_name='Pielęgnacja rośliny', null=True, blank=True)
    indoor = models.BooleanField(blank=True, null=True)
    outdoor = models.BooleanField(blank=True, null=True)
    pet_friendly = models.BooleanField(blank=True, null=True, verbose_name="Roślina przyjazna zwierzętom:")

    location = models.CharField(
        max_length=100, verbose_name="Lokalizacja:", null=True, blank=True)

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


class OfferGalleryImage(models.Model):
    offer_image = models.OneToOneField(OfferImage, on_delete=models.CASCADE, related_name='offergalleryimage', null=True, blank=True)
    gallery_image = models.ImageField(verbose_name="  ",
                                      null=True, blank=True,
                                      upload_to='products_pics/', default='products_pics/default.png')
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.offer.title} - Gallery Image'
