# Generated by Django 3.1.3 on 2021-02-10 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('racuni', '0005_auto_20210204_0013'),
        ('smjene', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='djelatniksmjenaprogram',
            unique_together={('djelatnik', 'smjena')},
        ),
    ]
