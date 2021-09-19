# Generated by Django 3.2.6 on 2021-09-19 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210919_0200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='indoor',
            field=models.BooleanField(default=False, verbose_name='Roślina outdoorowa:'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='negotiable',
            field=models.BooleanField(default=False, verbose_name='Cena do negocjacji:'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='outdoor',
            field=models.BooleanField(default=False, verbose_name='Roślina indoorowa:'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='pet_friendly',
            field=models.BooleanField(default=False, verbose_name='Roślina przyjazna zwierzętom:'),
        ),
    ]
