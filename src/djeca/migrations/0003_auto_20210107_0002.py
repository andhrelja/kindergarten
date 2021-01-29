# Generated by Django 3.1.3 on 2021-01-06 23:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('djeca', '0002_dijete_program'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dijetenapredak',
            name='djelatnik',
        ),
        migrations.AddField(
            model_name='dijetenapredak',
            name='autor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user', verbose_name='Autor'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dijetenapredak',
            name='ocjena',
            field=models.IntegerField(choices=[(5, 'Odličan'), (4, 'Vrlo dobar'), (3, 'Dobar'), (2, 'Dovoljan'), (1, 'Nedovoljan')], help_text='Ocjena djeteta u provedenom razdoblju', verbose_name='Ocjena'),
        ),
    ]