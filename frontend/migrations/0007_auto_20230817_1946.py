# Generated by Django 3.2.10 on 2023-08-17 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0006_applicationdb'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Employerregdb',
        ),
        migrations.DeleteModel(
            name='jobpostdb',
        ),
    ]
