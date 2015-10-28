from django.contrib import admin
from attend.models import Pessoa, Familia, Presenca, Turma
# from localflavor.br.forms import BRZipCodeField, BRPhoneNumberField, BRStateSelect


class PessoaAdmin(admin.ModelAdmin):
    fields = ('prenome', 'sobrenome', 'nascimento')
    list_display = ('prenome', 'sobrenome', 'nascimento')


class FamiliaAdmin(admin.ModelAdmin):
    fields = ('cep', 'endereco')
    list_display = ('cep', 'endereco')


class PresencaAdmin(admin.ModelAdmin):
    fields = ('data', 'pessoa', 'turma')
    list_display = ('data', 'pessoa', 'turma')


class TurmaAdmin(admin.ModelAdmin):
    fields = ('turma', 'horario')
    list_display = ('turma', 'horario')


admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Familia, FamiliaAdmin)
admin.site.register(Presenca, PresencaAdmin)
admin.site.register(Turma, TurmaAdmin)
