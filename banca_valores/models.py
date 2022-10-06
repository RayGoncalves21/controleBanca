from tabnanny import verbose
from django.db import models

class Banca_valor(models.Model):
   
    valor_inicial = models.FloatField(
        verbose_name="valor inicial",

    )

    def get_valor_incial(self):
        return self.valor_inicial
        
    

   
    class Meta:
        verbose_name ='Banca valor'
        verbose_name_plural ='Bancas valores',
        db_table ='banca_valor'

    def __str__(self):
        return self.valor_inicial
    
