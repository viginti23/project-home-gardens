# Generated by Django 3.2.6 on 2021-08-19 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='description',
            field=models.TextField(blank=True, max_length=512, null=True, verbose_name='Krótki opis:'),
        ),
    ]
