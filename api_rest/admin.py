from django.contrib import admin

from .models import Avaliacao, Desempenho, Plano, Treino, Usuario

admin.site.register(Avaliacao)
admin.site.register(Desempenho)
admin.site.register(Plano)
admin.site.register(Treino)
admin.site.register(Usuario)
