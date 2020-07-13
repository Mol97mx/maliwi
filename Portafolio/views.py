from django.shortcuts import render
from .models import Proyecto
from .models import Evento
from .models import Ubicacion
from .forms import ContactForm
#aqui que hay que hacer?

# Create your views here.

#def portafolio(request):
    #lista=ContactForm.objects.all()
    #return render(request,"portafolio/portafolio.html",{'nombre':lista})

def portafolio(request):
    contact_form= ContactForm()
    return render(request,"Portafolio/buscar.html",{'form':contact_form})

def resultado(request):#aqui se obtienien todos los resultados en el query set eventos, aqui hay que hacer el codigo de filtrado
    if request.method == "POST":
        datos = request.POST.copy()
        TE=datos.get("Tipo_evento")
        FI=datos.get("Fecha_inicio")
        FF=datos.get("Fecha_fin")
        e=Evento.objects.filter(Tipo_evento=TE)
        ev=e.filter(Fecha_inicio=FI)
        eventos=ev.filter(Fecha_fin=FF)
    return render(request,"Portafolio/resultado.html",{'evento':eventos})    