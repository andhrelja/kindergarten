# Generated by Django 3.1.3 on 2021-01-04 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('programi', '0006_auto_20201230_1310'),
        ('djeca', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dijete',
            name='program',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='programi.program', verbose_name='Upisani program'),
        ),
    ]
