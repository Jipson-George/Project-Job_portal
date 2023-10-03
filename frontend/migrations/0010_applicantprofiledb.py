# Generated by Django 3.2.10 on 2023-08-27 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0009_delete_applicationdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='applicantprofiledb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(blank=True, max_length=100, null=True)),
                ('Phone', models.CharField(max_length=100)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='Applicants')),
                ('Address', models.CharField(max_length=100)),
                ('Street', models.CharField(max_length=100)),
                ('City', models.CharField(max_length=100)),
                ('Nation', models.CharField(max_length=100)),
                ('Gender', models.CharField(max_length=100)),
                ('Ddate', models.CharField(max_length=100)),
                ('Dmonth', models.CharField(max_length=100)),
                ('Dyear', models.CharField(max_length=100)),
                ('Marital', models.CharField(max_length=100)),
                ('Pg', models.CharField(max_length=100)),
                ('Inst1', models.CharField(max_length=100)),
                ('Degree', models.CharField(max_length=100)),
                ('Inst2', models.CharField(max_length=100)),
                ('Tenth', models.CharField(max_length=100)),
                ('Inst3', models.CharField(max_length=100)),
                ('Others', models.CharField(max_length=100)),
                ('Inst4', models.CharField(max_length=100)),
                ('Skill1', models.CharField(max_length=100)),
                ('Skill2', models.CharField(max_length=100)),
                ('Skill3', models.CharField(max_length=100)),
                ('Exp', models.CharField(max_length=100)),
                ('Exp2', models.CharField(max_length=100)),
                ('Exp3', models.CharField(max_length=100)),
                ('Exp4', models.CharField(max_length=100)),
                ('Date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]