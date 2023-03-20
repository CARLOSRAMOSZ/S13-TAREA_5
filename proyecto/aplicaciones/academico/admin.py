from re import M
from django.contrib import admin
from aplicaciones.academico.models import Materias, Profesores

# Register your models here.

admin.site.register(Materias)
admin.site.register(Profesores)
