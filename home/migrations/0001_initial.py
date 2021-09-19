# Generated by Django 3.2.6 on 2021-09-18 21:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True, verbose_name='Nazwa przedmiotu:')),
                ('description', models.TextField(blank=True, max_length=1024, null=True, verbose_name='Opis:')),
                ('price', models.FloatField(null=True, verbose_name='Cena:')),
                ('negotiable', models.BooleanField(choices=[('Tak', 'Tak'), ('Nie', 'Nie')], default=False, verbose_name='Cena do negocjacji')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('size_category', models.CharField(choices=[('Roślina mała', 'Roślina mała'), ('Roślina średnia', 'Roślina średnia'), ('Roślina duża', 'Roślina duża'), ('Roślina bardzo duża', 'Roślina bardzo duża')], max_length=64, null=True, verbose_name='Wielkość rośliny:')),
                ('maintenance_category', models.CharField(choices=[('Roślina mało wymagająca', 'Roślina mało wymagająca'), ('Roślina średnio wymagająca', 'Roślina średnio wymagająca'), ('Roślina bardzo wymagająca', 'Roślina bardzo wymagająca')], max_length=64, null=True, verbose_name='Pielęgnacja rośliny:')),
                ('location', models.CharField(blank=True, max_length=100, null=True, verbose_name='Lokalizacja:')),
                ('seller', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Sprzedawca: ')),
            ],
        ),
        migrations.CreateModel(
            name='OfferImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='products_pics/default.png', upload_to='products_pics/', verbose_name='  ')),
                ('offer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.offer')),
            ],
        ),
        migrations.CreateModel(
            name='OfferGalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery_image', models.ImageField(default='products_pics/default.png', upload_to='products_pics/', verbose_name='  ')),
                ('offer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.offer')),
                ('offer_image', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='offergalleryimage', to='home.offerimage')),
            ],
        ),
    ]
