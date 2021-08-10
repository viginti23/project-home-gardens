# Generated by Django 3.2.5 on 2021-08-17 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offergalleryimage',
            name='offer_image',
        ),
        migrations.AddField(
            model_name='offerimage',
            name='offer_gallery_image',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='offergalleryimage', to='home.offergalleryimage'),
        ),
    ]
