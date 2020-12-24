# Generated by Django 3.1.3 on 2020-12-24 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vrtic', '0001_initial'),
        ('djeca', '0001_initial'),
        ('dogadjaji', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=128, verbose_name='Naziv programa')),
                ('dodatni_boravak', models.BooleanField(verbose_name='Dostupnost dodatnog boravka')),
                ('max_broj_djece', models.IntegerField(verbose_name='Maksimalni broj djece')),
            ],
            options={
                'verbose_name': 'Program',
                'verbose_name_plural': 'Programi',
            },
        ),
        migrations.CreateModel(
            name='VrstaPrograma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=128, verbose_name='Naziv programa')),
                ('opis', models.TextField(verbose_name='Opis vrste programa')),
                ('clanstvo_cijena', models.FloatField(help_text='Cijena mjesečne članarine', verbose_name='Cijena')),
                ('dobne_skupine', models.ManyToManyField(to='djeca.DobnaSkupina', verbose_name='Dobne skupine')),
                ('dogadjaji', models.ManyToManyField(blank=True, to='dogadjaji.Dogadjaj', verbose_name='Događaji')),
                ('vrtic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vrtic.vrtic', verbose_name='Vrtić')),
            ],
            options={
                'verbose_name': 'Vrsta programa',
                'verbose_name_plural': 'Vrste programa',
            },
        ),
    ]
