# Generated by Django 3.1.3 on 2020-12-24 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programi', '0002_auto_20201224_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='opis',
            field=models.TextField(default='', verbose_name='Opis programa'),
        ),
    ]