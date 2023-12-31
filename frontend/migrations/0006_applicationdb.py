# Generated by Django 3.2.10 on 2023-08-16 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0005_applicantregdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='applicationdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobid', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('mobile', models.IntegerField(blank=True, null=True)),
                ('company', models.CharField(max_length=100)),
                ('jobtitle', models.CharField(max_length=100)),
                ('cover', models.CharField(max_length=200)),
            ],
        ),
    ]
