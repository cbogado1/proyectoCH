from  django.template import Template, Context, loader
from django.http import HttpResponse

import datetime
def saludar(request):
    return HttpResponse("Bienvenidos a la comision 50215- Clase Django")
def bienvenido (request,nombre,apellido):
    respuesta = f"te damos la bienvenida a la comision 50215 {apellido},{nombre} "
    return HttpResponse(respuesta)

def bienvenido_html(request,nombre,apellido):
    hoy= datetime.datetime.now()
    respuesta = f"""
    <html>  
    <h1>Bienvenido al curso de Django!</h1>
    <h2>Esta es la comision 50215</h2>
    <h2>te damos la bienvenida a la comision 50215 {apellido},{nombre}</h2>
    <h3>Hoy es hoy  {hoy}</h3>
    </html>
    """
    return HttpResponse(respuesta)
def bienvenido_template(request):
    miHtml = open("C:/Users/CDjes/proyecto/proyecto/plantillas/bienvenido.html")
    plantilla = Template(miHtml.read())
    miHtml.close()
    contexto = Context()
    respuesta = plantilla.render(contexto)
    return HttpResponse(respuesta)

def bienvenido_template1(request):
    miHtml = open("C:/Users/CDjes/proyecto/proyecto/plantillas/bienvenido1.html")
    hoy= datetime.datetime.now()
    nombre = "Carlitos"
    apellido = "Carlos"
    contexto = {"nombre": nombre,"apellido": apellido, "hoy": hoy}
    plantilla = loader.get_template("C:/Users/CDjes/proyecto/proyecto/plantillas/bienvenido1.html")
    respuesta= plantilla.render(contexto)
    return HttpResponse(respuesta)