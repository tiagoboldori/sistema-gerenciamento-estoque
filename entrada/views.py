from django.shortcuts import render
from .models import *
from .forms import *
# Create your voews here.
#
def list_entrada(request):
    result = Entradas.objects.all()
    context = {
        'entradas':result,
    }
    return render(request, 'list_entrada.html', context)

