# Generated by Django 3.2.5 on 2021-08-06 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_category_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='name',
        ),
    ]
