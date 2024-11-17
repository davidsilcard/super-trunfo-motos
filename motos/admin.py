from django.contrib import admin
from .models import Moto

# Register your models here.
@admin.register(Moto)
class MotoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'ano', 'cilindrada', 'peso', 'preco')  # Colunas exibidas no admin
    search_fields = ('marca', 'modelo')  # Campos de pesquisa
    list_filter = ('ano', 'marca')  # Filtros laterais

