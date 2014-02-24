from django.contrib import admin
from libros.models import Libro, Autor

admin.site.register(Libro)
admin.site.register(Autor)