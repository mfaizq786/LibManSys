# Generated by Django 3.2.7 on 2021-10-21 09:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LibMangSys', '0011_alter_issuedbook_returndate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuedbook',
            name='issuedate',
            field=models.DateField(default=datetime.date(2021, 10, 21)),
        ),
        migrations.AlterField(
            model_name='issuedbook',
            name='returndate',
            field=models.DateField(default=datetime.date(2021, 10, 23)),
        ),
    ]
