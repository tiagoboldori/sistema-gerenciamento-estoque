from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Produtos 
from .forms import ProdutoForm 

# Create your views here.
def produto(request):
    return render(request, 'produto.html')

def list_produto(request):
    produtos = Produtos.objects.all()
    templateName = 'list_produto.html'
    context = {
        'produtos': produtos,   
    }
    return render(request, templateName, context)

def new_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_produto')
    else:
        templateName='new_produto.html'
        context = {
            'form': ProdutoForm()
        }
        return render(request, templateName, context)

def update_produto(request, pk):
    resultado = Produtos.objects.get(pk = pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance = resultado)
        if form.is_valid():
            form.save()
            return redirect('list_produto.html')
    else:
        form = ProdutoForm()
        context = {
            'item':resultado,
            'form': form,
            'pk':pk
        }
        return render(request, 'update_produto.html', context)

