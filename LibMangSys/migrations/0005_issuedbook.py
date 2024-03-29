# Generated by Django 3.2.7 on 2021-10-18 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LibMangSys', '0004_rename_catogory_book_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issuedbook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrollmentno', models.CharField(max_length=50)),
                ('bookno', models.CharField(max_length=30)),
                ('bookid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LibMangSys.book')),
                ('studid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LibMangSys.studentregistration')),
            ],
        ),
    ]
