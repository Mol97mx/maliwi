from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request,"nucleo/home.html")

def about(request):
     return render(request,"nucleo/about.html")


def contacto(request):
     return render(request,"nucleo/contacto.html")

