from django.contrib import admin
from .models import Receita


@admin.register(Receita)
class ReceitasAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_receita', 'publicada')
    list_editable = ('publicada',)
    list_display_links = ('id', 'nome_receita')
    search_fields = ('nome_receita', 'ingredientes',)
    list_filter = ('categoria',)
    list_per_page = 20
