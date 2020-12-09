# Generated by Django 3.1.3 on 2020-11-30 14:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('programi', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TipDjelatnika',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=50, verbose_name='Naziv tipa djelatnika')),
                ('strucni_tim', models.BooleanField(default=True, verbose_name='Pripada stručnom timu')),
                ('voditelj', models.BooleanField(default=False, verbose_name='Voditelj je')),
                ('tip_programa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programi.tipprograma', verbose_name='Tip programa')),
            ],
            options={
                'verbose_name': 'Tip djelatnika',
                'verbose_name_plural': 'Tipovi djelatnika',
            },
        ),
        migrations.CreateModel(
            name='Roditelj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefon', models.CharField(max_length=16, verbose_name='Kontakt telefon')),
                ('skrbnik', models.BooleanField(verbose_name='Skrbnik')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Django korisnik')),
            ],
            options={
                'verbose_name': 'Roditelj',
                'verbose_name_plural': 'Roditelji',
            },
        ),
        migrations.CreateModel(
            name='Djelatnik',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefon', models.CharField(max_length=16, verbose_name='Kontakt telefon')),
                ('tip_djelatnika', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='racuni.tipdjelatnika', verbose_name='Tip djelatnika')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Django korisnik')),
            ],
            options={
                'verbose_name': 'Djelatnik',
                'verbose_name_plural': 'Djelatnici',
            },
        ),
    ]