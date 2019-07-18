from django.shortcuts import render
from django.http import HttpResponse
from pendientes.models import Tarea

# Create your views here.

def index(request):
    listita = Tarea.objects.all()

    persona = {
        "nombre":"Fabio" ,
        "edad":21 ,
        "Hobbies": ["Futurismo","Comer", "aprender","caminar en las noches", "conocer historias","crear"],
        "lista_tareas": listita,
    }
    
    return render(request, "inicio.html", persona) #retornamos el saludo

def tarea(request):
    return HttpResponse("Hola! ya hice mi tarea")

def respuesta(request):
    return HttpResponse("La raza humana experimentara cambios colosales")
    
    