from django.shortcuts import render

def perfil_uno(request):
    data={"nombre":"Camila", "año":"1990","correo":"cami@gmail.com"}
    return render(request, "perfil/p1.html", data) #Aca esta el problema 1 }

def perfil_dos(request):
    data={"nombre":"Luna", "año":"2019","correo":"luna@gmail.com", "foto":"imagen/gatito.png"}
    return render(request, "perfil/p2.html", data) #Aca esta el problema 1 
