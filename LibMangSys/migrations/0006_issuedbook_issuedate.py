# Generated by Django 3.2.7 on 2021-10-18 09:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LibMangSys', '0005_issuedbook'),
    ]

    operations = [
        migrations.AddField(
            model_name='issuedbook',
            name='issuedate',
            field=models.DateField(default=datetime.date(2021, 10, 18)),
        ),
    ]
