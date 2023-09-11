from django.db import models

# from usuario.models import Usuario  # Certifique-se de importar o modelo de usuário corretamente

class Marca(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Camiseta(models.Model):
    nome = models.CharField(max_length=20)
    descricao = models.CharField(max_length=100)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="camisetas")
    tamanho = models.CharField(max_length=4)
    valor = models.DecimalField(max_digits=10, decimal_places=2)  # Corrija a definição do campo Decimal

    def __str__(self):
        return self.nome

class Bone(models.Model):
    nome = models.CharField(max_length=20, null=True, blank=True)
    descricao = models.CharField(max_length=100)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="bones")
    cor = models.CharField(max_length=10)
    valor = models.DecimalField(max_digits=10, decimal_places=2)  # Corrija a definição do campo Decimal

    def __str__(self):
        return f"{self.nome} ({self.cor})"

class Compra(models.Model):
    class StatusCompra(models.IntegerChoices):
        CARRINHO = 1, "Carrinho"
        REALIZADO = 2, "Realizado"
        PAGO = 3, "Pago"
        ENTREGUE = 4, "Entregue"

    # usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name="compras")
    status = models.IntegerField(choices=StatusCompra.choices, default=StatusCompra.CARRINHO)

    def __str__(self):
        return f"Compra de {self.usuario} - Status: {self.get_status_display()}"
