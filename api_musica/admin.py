from django.contrib import admin
from .models import Cancion, Genero, PerfilUsuario, Usuario

@admin.register(Cancion)
class CancionAdmin(admin.ModelAdmin):
    # Personaliza la configuración de la administración de Cancion si es necesario
    pass

@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    # Personaliza la configuración de la administración de Genero si es necesario
    pass

@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    
    pass

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    pass
