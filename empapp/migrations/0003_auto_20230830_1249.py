# Generated by Django 3.2.10 on 2023-08-30 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empapp', '0002_alter_applicationdb_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='companydb',
            name='status',
            field=models.CharField(default='Pending', max_length=100),
        ),
        migrations.AlterField(
            model_name='companydb',
            name='Description',
            field=models.CharField(max_length=300),
        ),
    ]
