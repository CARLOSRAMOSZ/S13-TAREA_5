from django.db import models

# Create your models here.

class Materias(models.Model):
    Codigo = models.CharField(primary_key=True, max_length=5)
    Asignatura = models.CharField(max_length=50)
    Duracion = models.PositiveSmallIntegerField(default=5)
    Asistencias = models.PositiveSmallIntegerField()
    def __str__(self):
      txt = "{0} (duracion: {1} año(s))"
      return txt.format(self.Asignatura, self.Duracion)

    
class Profesores(models.Model):
      cdi =models.CharField(max_length=8, primary_key=True)
      apellidomaterno = models.CharField(max_length=35)
      apellidopaterno = models.CharField(max_length=35)

      nombres =models.CharField(max_length=35)
      profesion =models.CharField(max_length=90)
      Fecha_de_Integración=models.DateField(auto_now_add=True)
      sexos = [
        ('F', 'Femenino'),
        ('M', 'Masculino')
      ]

      sexo = models.CharField(max_length=1, choices=sexos, default='F')  
      vigencia = models.BooleanField(default=True)
      carrera = models.ForeignKey(Materias, null=False, blank=False, on_delete=models.CASCADE)

      def nombreCompleto(self):
             txt = "{0} {1}, {2}"
             return txt.format(self.apellidomaterno, self.apellidopaterno, self.nombres)

      def __str__(self):
        txt = "{0} /Materias: {1} / {2}"
        if self.vigencia:
            estadoProfesores = "Vigente"
        else:
            estadoProfesores = "No Esta Registrado como profesor"
        return txt.format(self.nombreCompleto(), self.carrera, estadoProfesores)