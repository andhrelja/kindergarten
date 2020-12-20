# Generated by Django 3.1.3 on 2020-12-20 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('programi', '0001_initial'),
        ('racuni', '0003_auto_20201219_2136'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tipracuna',
            options={'verbose_name': 'Tip računa', 'verbose_name_plural': 'Tipovi računa'},
        ),
        migrations.AlterField(
            model_name='tipracuna',
            name='tip_programa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='programi.tipprograma', verbose_name='Tip programa'),
        ),
    ]