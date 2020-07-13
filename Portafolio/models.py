from django.db import models

# Create your models here.
class Proyecto(models.Model):
    titulo=models.CharField(max_length=200)
    descripcion= models.TextField()
    imagen=models.ImageField(upload_to="proyectos")
    creado=models.DateTimeField(auto_now_add=True)
    actualizado=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural="Proyectos"
        ordering=["-creado"]

    def __str__(self):
        return self.titulo

class Evento(models.Model):
    TipoGrupo = (
        ('D', 'Desprendimiento'),
        ('V', 'Vuelco'),
        ('DR', 'Deslizamiento Rotacional'),
        ('DT', 'Deslizamiento Traslacinal'),
        ('EL', 'Extensión Lateral'),
        ('F', 'Flujo'),
        ('C', 'Complejos'),
    )

    TipoMaterial = (
        ('R', 'Roca'),
        ('D', 'Detritos'),
        ('S', 'Suelo'),
    )

    id = models.AutoField(primary_key=True)
    Tipo_evento=models.CharField(max_length=2,choices=TipoGrupo,null=True)
    Tipo_material=models.CharField(max_length=1,choices=TipoMaterial,null=True)
    Fecha_inicio=models.DateField()
    Fecha_fin=models.DateField()
    Fuente=models.CharField(max_length=100,null=True)
    created=models.DateTimeField(auto_now_add=True,null=True)
    updated=models.DateTimeField(auto_now=True,null=True)
    Estado=models.CharField(max_length=25,null=True)
    Municipio=models.CharField(max_length=25,null=True)
    Longitud=models.FloatField(default=200,null=True)
    Latitud=models.FloatField(default=200,null=True)
    
    class Meta:
        verbose_name_plural="Eventos"
        ordering=["-created"]

    def __str__(self):
            return self.Tipo_material

class Ubicacion(models.Model):
    Estado=models.CharField(max_length=25,)
    Municipio=models.CharField(max_length=25,)
    Longitud=models.FloatField()
    Latitud=models.FloatField()