from django.contrib import admin
from .models import Pessoa


@admin.register(Pessoa)
class PessoasAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20
