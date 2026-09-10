from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "inicio/inicio.html") # Va estar renderizando la plantilla index.html que se encuentra en la carpeta templates