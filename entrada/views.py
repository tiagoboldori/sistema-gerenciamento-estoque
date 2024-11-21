from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import HttpResponse
# Create your voews here.
#
def list_entrada(request):
    result = Entradas.objects.all().order_by('-id')
    context = {
        'entradas':result,
    }
    return render(request, 'list_entrada.html', context)


def new_entrada(request):
    if request.method == 'POST':
        form = EntradasForm(request.POST)
        if form.is_valid():
            flag = False
            form.save(commit=False)
            form.cleaned_data['produto'].quantidade += form.cleaned_data['quantidade']
            if form.cleaned_data['preco'] == 0:
                flag = True
                form.cleaned_data['preco'] = form.cleaned_data['produto'].preco
                price = form.cleaned_data['produto'].preco
            form.cleaned_data['produto'].preco = form.cleaned_data['preco']
            form.cleaned_data['produto'].save_base()

            temp = form.save()
            
            if flag:
                result = Entradas.objects.get(pk=temp.id)
                result.preco = price
                result.save()
            return redirect('list_entrada')
    else:
        form = EntradasForm()
        context={
            'form': form
        }
        return render(request, 'new_entrada.html',context)


def remove_entrada(request,pk):
    result = Entradas.objects.get(pk = pk)
    result.delete()
    return redirect('list_entrada') 
