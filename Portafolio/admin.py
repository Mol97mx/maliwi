from django.contrib import admin
from .models import Proyecto
from .models import Evento
from .models import Ubicacion
# Register your models here.
class ProjectAdmin (admin.ModelAdmin):
    readonly_fields=("creado","actualizado")
admin.site.register(Proyecto, ProjectAdmin)
admin.site.register(Evento)
admin.site.register(Ubicacion)