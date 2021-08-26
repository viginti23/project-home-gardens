from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Offer(models.Model):
    SIZE_CHOICES = [
        ('Roślina mała', 'Roślina mała'),
        ('Roślina średnia', 'Roślina średnia'),
        ('Roślina duża', 'Roślina duża'),
        ('Roślina bardzo duża', 'Roślina bardzo duża'),
    ]
    MAINTENANCE_CHOICES = [
        ('Roślina mało wymagająca', 'Roślina mało wymagająca'),
        ('Roślina średnio wymagająca', 'Roślina średnio wymagająca'),
        ('Roślina bardzo wymagająca', 'Roślina bardzo wymagająca'),
    ]
    title = models.CharField(
        max_length=100, verbose_name="Nazwa przedmiotu:", null=True, blank=False)
    description = models.TextField(
        max_length=1024, verbose_name="Opis:", null=True, blank=True)
    price = models.FloatField(verbose_name="Cena:", null=True, blank=False)
    negotiable = models.BooleanField(verbose_name='Do negocjacji', default=False)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Sprzedawca: ')
    date_posted = models.DateTimeField(default=timezone.now)
    size_category = models.CharField(max_length=64, verbose_name='Wielkość rośliny:', null=True, blank=False,
                                     choices=SIZE_CHOICES)
    maintenance_category = models.CharField(max_length=64, verbose_name='Pielęgnacja rośliny:', null=True, blank=False,
                                            choices=MAINTENANCE_CHOICES)

    indoor = models.BooleanField(blank=False, null=True, verbose_name='Roślina outdoorowa:', default=False)
    outdoor = models.BooleanField(blank=False, null=True, verbose_name='Roślina indoorowa:', default=False)
    pet_friendly = models.BooleanField(blank=False, null=True,
                                       verbose_name="Roślina przyjazna zwierzętom:", default=False)

    location = models.CharField(
        max_length=100, verbose_name="Lokalizacja:", null=True, blank=True)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self, *args, **kwargs):
        return reverse('offerdetail', kwargs={'pk': self.pk})


class OfferImage(models.Model):
    image = models.ImageField(verbose_name="  ",
                              upload_to='products_pics/', default='products_pics/default.png')

    offer = models.ForeignKey(
        Offer, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.offer.title} - Photo'


class OfferGalleryImage(models.Model):
    offer_image = models.OneToOneField(OfferImage, on_delete=models.CASCADE, related_name='offergalleryimage',
                                       null=True)
    gallery_image = models.ImageField(verbose_name="  ",
                                      upload_to='products_pics/', default='products_pics/default.png')
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.offer.title} - Gallery Image'
