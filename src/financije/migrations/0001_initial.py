# Generated by Django 3.1.3 on 2020-12-21 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('djeca', '0001_initial'),
        ('racuni', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RacunClanarina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=128, verbose_name='Naziv dokumenta')),
                ('datum', models.DateTimeField(auto_now_add=True, verbose_name='Datum dokumenta')),
                ('iznos', models.FloatField(verbose_name='Iznos')),
                ('PDV', models.FloatField(default=25.0, verbose_name='PDV (%)')),
                ('ukupno', models.FloatField(verbose_name='Ukupno')),
                ('dijete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djeca.dijete', verbose_name='Dijete')),
            ],
            options={
                'verbose_name': 'Račun - članarina',
                'verbose_name_plural': 'Računi - članarine',
            },
        ),
        migrations.CreateModel(
            name='PlacaDjelatnik',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=50, verbose_name='Naziv dokumenta')),
                ('datum', models.DateTimeField(auto_now_add=True, verbose_name='Datum dokumenta')),
                ('bruto', models.FloatField(verbose_name='Bruto iznos plaće')),
                ('neto', models.FloatField(verbose_name='Neto iznos plaće')),
                ('tip_djelatnika', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='racuni.tipracuna', verbose_name='Tip djelatnika')),
            ],
            options={
                'verbose_name': 'Plaća - djelatnik',
                'verbose_name_plural': 'Plaće - djelatnici',
            },
        ),
    ]
