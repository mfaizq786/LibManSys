# Generated by Django 3.2.7 on 2021-10-20 10:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LibMangSys', '0010_alter_issuedbook_returndate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuedbook',
            name='returndate',
            field=models.DateField(default=datetime.date(2021, 10, 22)),
        ),
    ]
