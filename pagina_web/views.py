from datetime import datetime

from django.shortcuts import render 
from django.http import HttpResponse

def saludar(request): 
    saludo = "Hola querido usuario"
    pagina_html = HttpResponse(saludo)
    return pagina_html 

def saludar_con_fecha(request):
    hoy = datetime.now().day
    saludo = f"Hola usuario, fecha:{hoy} "
    pagina_html = HttpResponse(saludo)
    return pagina_html 

def saludar_con_html(request):
    contexto = {}
    http_response = render(
        request=request, template_name='AppCoder/base.html', context=contexto)
    return http_response
