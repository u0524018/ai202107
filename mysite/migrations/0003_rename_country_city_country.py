# Generated by Django 3.2.5 on 2021-07-13 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_city_country'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='Country',
            new_name='country',
        ),
    ]
