from django.db import models

# Organização por marcas (Ex: Coral, Suvinil)
class Marca(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    def __str__(self): return self.nome

# Modelo de Produto para consulta instantânea no balcão
class Produto(models.Model):
    nome = models.CharField(max_length=200)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    cor = models.CharField(max_length=50)
    tamanho = models.CharField(max_length=50) # Ex: 18L, 3.6L
    quantidade_estoque = models.IntegerField(default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nome} {self.cor} - {self.tamanho}"

# Sistema de fidelização: 20 pontos por cada R$ 1,00 de desconto
class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=11, unique=True)
    pontos = models.IntegerField(default=0)
