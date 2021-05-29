from django.shortcuts import render, redirect

def servicios(request):
    return render(request,'menu_opciones.html')