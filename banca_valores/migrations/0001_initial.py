# Generated by Django 3.0 on 2022-09-27 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banca_valor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banca', models.CharField(max_length=194, verbose_name='Banca')),
                ('valor_inicial', models.FloatField(verbose_name='valor inicial')),
            ],
        ),
    ]
