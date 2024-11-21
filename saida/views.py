from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.


def list_saida(request):
    result = Saidas.objects.all().order_by('-id')
    context = {
        'saidas':result
    }
    return render(request, 'list_saida.html', context)

def new_saida(request):
    if request.method=="POST":
        form = SaidasForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            if form.cleaned_data['produto'].quantidade >= form.cleaned_data['quantidade']:
                form.cleaned_data['produto'].quantidade -= form.cleaned_data['quantidade']
                form.cleaned_data['produto'].save_base()
                form.save()
                return redirect('list_saida')
            else:
                return HttpResponse('Quantidade Insuficiente')
    else:
        form = SaidasForm()
        context = {
            'form':form
        }
        return render(request, 'new_saida.html', context)

def remove_saida(request, pk):
    result = Saidas.objects.get(pk = pk)
    result.delete()
    return redirect('list_saida')
