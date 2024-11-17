from django.db import models

# Create your models here.
class Moto(models.Model):
    # Campos principais
    marca = models.CharField(max_length=100)  # Ex: Honda, Yamaha
    modelo = models.CharField(max_length=100)  # Ex: CB 500, XTZ 125
    ano = models.IntegerField()  # Ex: 2020
    cilindrada = models.IntegerField(help_text="Em cm³")  # Ex: 500
    peso = models.DecimalField(max_digits=5, decimal_places=2, help_text="Em kg")  # Ex: 170.5
    preco = models.DecimalField(max_digits=10, decimal_places=2, help_text="Em R$")  # Ex: 35000.99

    # Para exibir corretamente no Django Admin
    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.ano})"
