# Generated by Django 3.2.10 on 2023-08-29 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='job_typedb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobtype', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='jobdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobcat', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='verifiedjobdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Jobid', models.IntegerField(blank=True, null=True)),
                ('Title', models.CharField(max_length=100)),
                ('User', models.CharField(max_length=100)),
                ('Company', models.CharField(max_length=100)),
                ('Type', models.CharField(max_length=100)),
                ('Category', models.CharField(max_length=100)),
                ('Qualification', models.CharField(max_length=100)),
                ('Location', models.CharField(max_length=100)),
                ('Experiance', models.CharField(max_length=100)),
                ('Salary', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=200)),
                ('Date', models.DateField(auto_now_add=True)),
                ('approval', models.CharField(default='verified', max_length=100)),
                ('Requirement', models.CharField(blank=True, max_length=100, null=True)),
                ('website', models.CharField(blank=True, max_length=100, null=True)),
                ('Cemail', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
