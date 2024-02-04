# Generated by Django 3.2.7 on 2021-10-20 10:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LibMangSys', '0006_issuedbook_issuedate'),
    ]

    operations = [
        migrations.AddField(
            model_name='issuedbook',
            name='returndate',
            field=models.DateField(default=datetime.date(2021, 11, 5)),
        ),
        migrations.AlterField(
            model_name='issuedbook',
            name='issuedate',
            field=models.DateField(default=datetime.date(2021, 10, 20)),
        ),
    ]
