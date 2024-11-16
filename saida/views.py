from django.shortcuts import render

# Create your views here.


def list_saida(request):
    result = Saidas.objects.all()
    context = {
        'saidas':result
    }
    return render(request, 'list_saida.html', context)

def new_saida(request):
    pass


def remove_saida(request):
    pass
