from django.contrib import admin
from django.urls import path
from inventario import views

urlpatterns = [
    # Admin do Django
    path('admin/', admin.site.urls),

    # 🔐 Autenticação
    path('', views.tela_login, name='login'),
    path('logout/', views.logout, name='logout'),

    # 📊 Painel Principal
    path('painel/', views.painel_principal, name='painel_principal'),

    # 🛒 Frente de Caixa (PDV)
    path('pdv/', views.tela_pdv, name='tela_pdv'),
    path('api/buscar-produtos/', views.api_buscar_produtos, name='api_buscar_produtos'),
    path('api/salvar-venda/', views.api_salvar_venda, name='api_salvar_venda'),
    path('api/consultar-pontos/', views.api_consultar_pontos, name='api_consultar_pontos'),

    # 📦 Controle de Estoque
    path('estoque/', views.tela_estoque_produtos, name='tela_estoque_produtos'),
    path('estoque/salvar/', views.salvar_produto, name='salvar_produto'),
    path('estoque/excluir/<int:id>/', views.excluir_produto, name='excluir_produto'),
    path('estoque/carga/', views.tela_entrada_carga, name='tela_entrada_carga'),

    # 👥 Gestão de Clientes e Pintores
    path('clientes/', views.tela_consultar_clientes, name='tela_consultar_clientes'),
    path('clientes/salvar/', views.salvar_edicao_cliente, name='salvar_edicao_cliente'),
    path('api/historico-cliente/', views.api_historico_cliente, name='api_historico_cliente'),

    # ⚙️ Submenus Auxiliares (Marcas e Famílias Separadas)
    path('marcas/', views.tela_marcas, name='tela_marcas'),
    path('marcas/salvar/', views.salvar_marca, name='salvar_marca'),
    path('marcas/excluir/<int:id>/', views.excluir_marca, name='excluir_marca'),

    path('familias/', views.tela_familias, name='tela_familias'),
    path('familias/salvar/', views.salvar_familia, name='salvar_familia'),
    path('familias/excluir/<int:id>/', views.excluir_familia, name='excluir_familia'),

    # 🔄 ROTA DE COMPATIBILIDADE: Evita o erro NoReverseMatch nos templates antigos
    path('auxiliares/', views.tela_marcas, name='tela_gerencia_auxiliares'),

    # 📊 Relatórios Financeiros e Cupons
    path('relatorios/', views.tela_relatorios, name='tela_relatorios'),
    path('venda/cupom/<int:id>/', views.imprimir_cupom, name='imprimir_cupom'),
    path('venda/cupom-a4/<int:id>/', views.imprimir_cupom_a4, name='imprimir_cupom_a4'),

    # 👥 Gestão de Equipe (Colaboradores JB)
    path('colaboradores/', views.tela_colaboradores, name='tela_colaboradores'),
    path('colaboradores/salvar/', views.salvar_colaborador, name='salvar_colaborador'),
    path('colaboradores/excluir/<int:id>/', views.excluir_colaborador, name='excluir_colaborador'),

    # ⚙️ Configuração de Regras de Fidelidade
    path('fidelidade/', views.tela_manutencao_pontos, name='tela_manutencao_pontos'),
    path('fidelidade/salvar/', views.salvar_configuracao_pontos, name='salvar_configuracao_pontos'),
]