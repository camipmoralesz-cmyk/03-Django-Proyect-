from django.shortcuts import render


def v1(request):
    return render (request,"app1/v1.html")

def v2(request):
    return render (request,"app1/v2.html")
# Create your views here.
