# Generated by Django 3.1.3 on 2021-02-02 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('racuni', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='racun',
            name='tip_racuna',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='racuni.tipracuna', verbose_name='Uloga korisnika'),
        ),
    ]
