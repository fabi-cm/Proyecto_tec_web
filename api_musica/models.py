from django.db import models
from django.contrib.auth.models import User


class Genero(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre.upper()


class Cancion(models.Model):
    titulo = models.CharField(max_length=100, default="Desconocido")
    artista = models.CharField(max_length=100, default="Desconocido")
    imagen_portada = models.ImageField(upload_to="canciones", default="default.png")
    duracion = models.PositiveIntegerField(default=0)
    genero = models.ManyToManyField(Genero)

    def __str__(self):
        return "{0} De: {1}".format(self.titulo, self.artista)


class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen_perfil = models.ImageField(upload_to="perfil", default="default_perfil.png")

    def __str__(self):
        return "Perfil de: {0}".format(self.user.username)

class Usuario(models.Model):
    username = models.CharField(max_length=50, unique=True, verbose_name='Username', blank=False)
    nombre = models.CharField(max_length=255, verbose_name="Nombre", blank=True)
    apellido = models.CharField(max_length=255, verbose_name="Apellidos", blank=True)
    imagen_perfil = models.ImageField(upload_to="usuarios", default="default_perfil.png")
    correo = models.EmailField(verbose_name="Correo electronico", blank=True)
    password = models.CharField(max_length=250, verbose_name="Password", blank=False)
    biblioteca = models.ManyToManyField(Cancion)

    def __str__(self):
        return self.username
