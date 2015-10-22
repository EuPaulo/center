from django.db import models
from localflavor.br.forms import BRZipCodeField, BRPhoneNumberField, BRStateSelect


class Turma(models.Model):
    turma = models.CharField(max_length=50)
    horario = models.CharField(max_length=50)

class Pessoa(models.Model):
    prenome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length = 70)
    nascimento = models.DateField()
    pai = models.CharField(max_length=100)
    mae = models.CharField(max_length=100)
    saida = models.NullBooleanField()
    turma = models.ForeignKey(Turma)

class Presenca(models.Model):
    data = models.DateField
    pessoa = models.ForeignKey(Pessoa)
    turma = models.ForeignKey(Turma)

class Familia(models.Model):
    CEP = BRZipCodeField() 
    telefone = BRPhoneNumberField()
    endereco = models.CharField(max_length=200)
    estado = BRStateSelect()


class Natal(models.Model):
    ano = models.IntegerField 
    camisa = models.CharField(max_length=30)
    bermuda = models.CharField(max_length=30)
    sapato = models.CharField(max_length=30)

class Relacionamento(models.Model):
    individuo1 = models.ForeignKey(Pessoa, related_name="idindividuo1") 
    individuo2 = models.ForeignKey(Pessoa, related_name="idindividuo2")
    relacionamento = models.CharField(max_length=100)

