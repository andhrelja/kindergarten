# Generated by Django 3.1.3 on 2020-12-19 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djeca', '0002_auto_20201130_1550'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dijete',
            name='tip_programa',
        ),
    ]