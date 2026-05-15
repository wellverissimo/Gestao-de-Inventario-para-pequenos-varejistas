from django.shortcuts import render
from .models import Produto
from django.db.models import Q

def consulta_estoque(request):
    termo_busca = request.GET.get('q', '')
    
    if termo_busca:
        produtos = Produto.objects.filter(
            Q(nome__icontains=termo_busca) | 
            Q(marca__nome__icontains=termo_busca) | 
            Q(cor__icontains=termo_busca)
        )
    else:
        produtos = Produto.objects.all()

    return render(request, 'inventario/busca.html', {'produtos': produtos, 'query': termo_busca})