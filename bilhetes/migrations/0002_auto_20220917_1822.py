# Generated by Django 3.0 on 2022-09-17 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bilhetes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bilhete',
            name='time_casa',
            field=models.CharField(blank=True, max_length=194, null=True, verbose_name='Time jogando em casa'),
        ),
        migrations.AlterField(
            model_name='bilhete',
            name='time_fora',
            field=models.CharField(blank=True, max_length=194, null=True, verbose_name='Time jogando fora'),
        ),
    ]
