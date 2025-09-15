from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def vista1(request):
    return HttpResponse(
        """
        <h1>Vista 1</h1>
        <p style="color:blue;">un 7 por favor ¿si? :)<p>
        <a href="/aplicacion1/Vista2">Vista 2</a>
        """
        )
def vista2(request):
    return HttpResponse(
        """
        <h1>Vista 2</h1>
        <p style="color:blue;">otro 7 por favor ¿oki? (:<p>
        <a href="/aplicacion1/vista1">Vista 1</a>
        """
        )