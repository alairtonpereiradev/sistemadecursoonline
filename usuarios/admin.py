from django.contrib import admin
from .models import Usuario
from django.contrib.admin.decorators import display

# Register your models here.

#admin.site.register(Usuario)

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'senha')
    search_fields = ('nome', 'email')
    readonly_fields = ('senha',)