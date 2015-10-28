from django.db import models


class Turma(models.Model):
    turma = models.CharField(max_length=50)
    horario = models.CharField(max_length=50)


class Pessoa(models.Model):
    prenome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=70, blank=True)
    nascimento = models.DateField(blank=True, null=True)
    pai = models.CharField(max_length=100, blank=True, null=True)
    mae = models.CharField(max_length=100, blank=True, null=True)
    saida = models.NullBooleanField(blank=True, null=True)
    turma = models.ForeignKey(Turma, blank=True, null=True)


class Presenca(models.Model):
    data = models.DateField()
    pessoa = models.ForeignKey(Pessoa)
    turma = models.ForeignKey(Turma)


class Familia(models.Model):
    cep = models.CharField(max_length=9)
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=200)


class Natal(models.Model):
    ano = models.IntegerField()
    camisa = models.CharField(max_length=30)
    bermuda = models.CharField(max_length=30)
    sapato = models.CharField(max_length=30)


class Relacionamento(models.Model):
    individuo1 = models.ForeignKey(Pessoa, related_name="idindividuo1")
    individuo2 = models.ForeignKey(Pessoa, related_name="idindividuo2")
    relacionamento = models.CharField(max_length=100)
