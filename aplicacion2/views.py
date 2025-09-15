from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def mirada1(request):
    return HttpResponse(
        """
        <h1>Mirada 1</h1>
        <p style="color:blue;">doneme un 7 adicional para mi fundacion 'notas' porfii :D</p>
        <a href="/aplicacion2/vista2">mirada 2</a>
        """
        )
def mirada2(request):
    return HttpResponse(
        """
        <h1>Mirada 2</h1>
        <p style="color:blue;">¿y me podria regalar un 7 mas adicional solo por las moscas? C:</p>
        <a href="/aplicacion2/vista1">mirada 1</a>
        """
        )