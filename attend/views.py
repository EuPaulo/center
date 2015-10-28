from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
# from django.contrib.auth.decorators import login_required
from django import forms

from models import Pessoa
from forms import FormPessoa


# @login_required
def pessoa(request):
    lista_pessoa = Pessoa.objects.all()
    return render_to_response('attend/pessoa.html', {'pessoa': lista_pessoa},
                              context_instance=RequestContext(request))


def adicionaPessoa(request):
    if request.method == "POST":
        form = FormPessoa(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            return render_to_response("attend/salvo.html", {})
        else:
            raise forms.ValidationError(('Valor incorreto'), code='invalid')
    else:
        form = FormPessoa()
        return render_to_response("attend/adiciona.html", {'form': form},
                                  context_instance=RequestContext(request))


def editaPessoa(request, id_pessoa):
    item = get_object_or_404(Pessoa, pk=id_pessoa)
    if request.method == "POST":
        form = FormPessoa(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            return render_to_response("attend/salvo.html", {})
        else:
            raise forms.ValidationError(('Valor incorreto'), code='invalid')
    else:
        form = FormPessoa(instance=item)
        return render_to_response("attend/item.html", {'form': form},
                                  context_instance=RequestContext(request))


def removePessoa(request, id_pessoa):
    item = get_object_or_404(Pessoa, pk=id_pessoa)
    if request.method == "POST":
        item.delete()
        return render_to_response("attend/removido.html", {})
    return render_to_response("attend/remove.html", {'item': item},
                              context_instance=RequestContext(request))
