from django import forms
from models import Pessoa


class FormPessoa(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ('prenome',
                  'sobrenome',
                  'nascimento',
                  'pai',
                  'mae',
                  'saida',
                  'turma')
