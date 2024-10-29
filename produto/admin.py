from django.contrib import admin
from .models import *
# Register your models here.
class ProdutosAdmin(admin.ModelAdmin): 
    list_display = [ 
        'produto', 
        'cor', 
        'preco', 
        'quantidade', 
    ] 
admin.site.register(Produtos, ProdutosAdmin) 
admin.site.register(Cores)