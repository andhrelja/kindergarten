# Generated by Django 3.1.3 on 2021-02-08 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financije', '0004_auto_20210208_2120'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clanarina',
            options={'ordering': ['-datum'], 'verbose_name': 'Članarina', 'verbose_name_plural': 'Članarine'},
        ),
        migrations.AlterModelOptions(
            name='placa',
            options={'ordering': ['-datum'], 'verbose_name': 'Plaća', 'verbose_name_plural': 'Plaće'},
        ),
    ]