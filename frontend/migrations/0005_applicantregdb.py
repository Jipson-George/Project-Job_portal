# Generated by Django 3.2.10 on 2023-08-14 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0004_rename_vaccancy_jobpostdb_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='applicantregdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('Mobile', models.IntegerField(blank=True, null=True)),
                ('Password', models.CharField(max_length=100)),
            ],
        ),
    ]