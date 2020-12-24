# Generated by Django 3.1.3 on 2020-12-24 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dogadjaj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=50, verbose_name='Naziv')),
                ('opis', models.TextField(verbose_name='Opis događaja')),
                ('adresa', models.CharField(max_length=255, verbose_name='Lokacija događaja')),
                ('datum_start', models.DateField(verbose_name='Datum početka')),
                ('datum_kraj', models.DateField(verbose_name='Datum kraja')),
                ('vrijeme_start', models.TimeField(verbose_name='Vrijeme početka')),
                ('vrijeme_kraj', models.TimeField(verbose_name='Vrijeme kraja')),
            ],
            options={
                'verbose_name': 'Događaj',
                'verbose_name_plural': 'Događaji',
            },
        ),
    ]
