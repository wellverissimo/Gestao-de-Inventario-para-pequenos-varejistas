# Estrutura de busca que faz o filtro por nome, marca ou cor
from django.shortcuts import render
from .models import Produto
from django.db.models import Q

def consulta_estoque(request):
    # Captura o que o atendente digitou na barra de busca
    termo_busca = request.GET.get('q', '')
    
    # Se houver busca, filtra os 2.539 itens por Nome, Marca ou Cor
    if termo_busca:
        produtos = Produto.objects.filter(
            Q(nome__icontains=termo_busca) | 
            Q(marca__nome__icontains=termo_busca) | 
            Q(cor__icontains=termo_busca)
        )
    else:
        # Se estiver vazio, mostra todos (ou nenhum, dependendo da preferência)
        produtos = Produto.objects.all()

    # Envia os resultados para a página web (HTML)
    return render(request, 'inventario/busca.html', {'produtos': produtos, 'query': termo_busca})
