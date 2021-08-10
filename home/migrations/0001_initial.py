# Generated by Django 3.2.5 on 2021-08-16 21:58

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
            name='MaintenanceCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=60, null=True)),
            ],
            options={
                'verbose_name_plural': 'maintenance categories',
            },
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nazwa przedmiotu:')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='Opis:')),
                ('price', models.FloatField(blank=True, null=True, verbose_name='Cena:')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('negotiable', models.BooleanField(default=True, verbose_name='Do negocjacji')),
                ('maintenance_category', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='home.maintenancecategory', verbose_name='Pielęgnacja rośliny')),
                ('seller', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Sprzedawca: ')),
            ],
        ),
        migrations.CreateModel(
            name='SizeCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=25, null=True)),
            ],
            options={
                'verbose_name_plural': 'size categories',
            },
        ),
        migrations.CreateModel(
            name='OfferImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='products_pics/default.png', null=True, upload_to='products_pics/', verbose_name='  ')),
                ('offer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.offer')),
            ],
        ),
        migrations.CreateModel(
            name='OfferGalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery_image', models.ImageField(blank=True, default='products_pics/default.png', null=True, upload_to='products_pics/', verbose_name='  ')),
                ('offer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.offer')),
                ('offer_image', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.offerimage')),
            ],
        ),
        migrations.AddField(
            model_name='offer',
            name='size_category',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='home.sizecategory', verbose_name='Wielkość rośliny'),
        ),
    ]
