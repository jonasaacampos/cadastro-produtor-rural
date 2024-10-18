from django.db import models
from django.core.exceptions import ValidationError

class PropriedadeRural(models.Model):
    nome = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=2)
    area_total = models.FloatField()
    area_agricultavel = models.FloatField()
    area_vegetacao = models.FloatField()
    culturas = models.CharField(max_length=255)

    def clean(self):
        if self.area_agricultavel + self.area_vegetacao > self.area_total:
            raise ValidationError('A soma da área agricultável e vegetação não pode ser maior que a área total da fazenda.')
        

class ProdutorRural(models.Model):
    cpf_cnpj = models.CharField(max_length=18, unique=True)
    nome = models.CharField(max_length=255)
    fazendas = models.ManyToManyField(PropriedadeRural)