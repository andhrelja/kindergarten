# Generated by Django 3.1.3 on 2021-02-10 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smjene', '0002_auto_20210210_1313'),
        ('djeca', '0004_dijete_smjena'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dijete',
            name='smjena',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smjene.smjena', verbose_name='Smjena čuvanja'),
        ),
    ]
