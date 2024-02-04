# Generated by Django 3.2.7 on 2021-10-12 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=30, verbose_name='first name')),
                ('lname', models.CharField(max_length=30, verbose_name='last name')),
                ('enrollno', models.CharField(max_length=30, verbose_name='enrollmentno')),
                ('branch', models.CharField(max_length=10, verbose_name='branch')),
                ('image', models.ImageField(upload_to='images')),
                ('username', models.CharField(max_length=30, verbose_name='username')),
                ('password', models.CharField(max_length=20, verbose_name='password')),
            ],
        ),
    ]