from django.db import models


class Dinheiro(models.Model):

    banca_nome = models.CharField(
        verbose_name='Nome da Banca',
        max_length=100

    )

    banca_valor = models.DecimalField(
        verbose_name='Valor da Banca hoje R$',
        max_digits=25,
        decimal_places=2,
        max_length=50
    )

    class Meta:
        verbose_name = 'Banca',
        verbose_name_plural = 'Bancas',
        db_table = 'dinheiro'

    def __str__(self):
        return self.banca_nome
