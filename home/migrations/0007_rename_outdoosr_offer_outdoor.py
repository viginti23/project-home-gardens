# Generated by Django 3.2.6 on 2021-08-30 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_rename_outdoor_offer_outdoosr'),
    ]

    operations = [
        migrations.RenameField(
            model_name='offer',
            old_name='outdoosr',
            new_name='outdoor',
        ),
    ]
