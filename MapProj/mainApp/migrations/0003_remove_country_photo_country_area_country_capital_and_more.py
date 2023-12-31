# Generated by Django 4.2.5 on 2023-10-03 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_trip_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='photo',
        ),
        migrations.AddField(
            model_name='country',
            name='area',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='country',
            name='capital',
            field=models.CharField(blank=True, max_length=100, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='country',
            name='part',
            field=models.CharField(blank=True, max_length=100, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='country',
            name='population',
            field=models.IntegerField(default=0),
        ),
    ]
