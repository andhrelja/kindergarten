# Generated by Django 3.1.3 on 2021-02-03 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racuni', '0002_auto_20210202_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipracuna',
            name='je_djelatnik',
            field=models.BooleanField(null=True, verbose_name='Djelatnik'),
        ),
        migrations.AddField(
            model_name='tipracuna',
            name='je_roditelj',
            field=models.BooleanField(null=True, verbose_name='Roditelj'),
        ),
        migrations.AddField(
            model_name='tipracuna',
            name='je_voditelj',
            field=models.BooleanField(null=True, verbose_name='Voditelj'),
        ),
    ]
