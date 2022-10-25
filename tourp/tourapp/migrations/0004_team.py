# Generated by Django 3.2.15 on 2022-08-22 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourapp', '0003_delete_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('img', models.ImageField(upload_to='pics')),
                ('desc', models.TextField()),
            ],
        ),
    ]
