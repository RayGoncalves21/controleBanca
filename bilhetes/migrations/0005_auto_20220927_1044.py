# Generated by Django 3.0 on 2022-09-27 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bilhetes', '0004_auto_20220917_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bilhete',
            name='status',
            field=models.CharField(choices=[('AGUARDANDO', 'Aguardando'), ('GREEN', 'Green'), ('RED', 'Red')], default='AGUARDANDO', max_length=194, verbose_name='status'),
        ),
    ]