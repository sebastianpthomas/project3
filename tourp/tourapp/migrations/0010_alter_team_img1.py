# Generated by Django 3.2.15 on 2022-08-23 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourapp', '0009_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='img1',
            field=models.ImageField(upload_to='pics'),
        ),
    ]
