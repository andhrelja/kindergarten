# Generated by Django 3.1.3 on 2021-02-08 20:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('financije', '0002_auto_20210205_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='clanarina',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Datum stvaranja'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='clanarina',
            name='datum',
            field=models.DateField(verbose_name='Datum dokumenta'),
        ),
    ]
