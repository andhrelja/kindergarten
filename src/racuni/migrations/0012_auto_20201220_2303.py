# Generated by Django 3.1.3 on 2020-12-20 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racuni', '0011_auto_20201220_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upis',
            name='odobren',
            field=models.BooleanField(null=True, verbose_name='Zahtjev odobren'),
        ),
    ]
