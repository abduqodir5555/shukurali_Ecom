# Generated by Django 5.0.3 on 2024-04-12 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='file',
            field=models.FileField(upload_to='files/', verbose_name='File'),
        ),
    ]
