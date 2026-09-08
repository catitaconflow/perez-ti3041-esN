from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hola, esta es la app catálogo.")

import json
from django.shortcuts import render
from django.http import HttpResponseNotFound
from pathlib import Path

def detalle_herramienta(request, id):
    ruta = Path(__file__).resolve().parent / "data" / "herramientas.json"
    with open(ruta, encoding="utf-8") as f:
        herramientas = json.load(f)

    print("Herramientas cargadas:", herramientas[:3])  # muestra los primeros registros
    print("Buscando id:", id)

    herramienta = next((h for h in herramientas if h.get("id") == id), None)

    if herramienta is None:
        return HttpResponseNotFound("<h2>Herramienta no encontrada</h2>")

    return render(request, "catalogo/detalle.html", {"herramienta": herramienta})

def listado_herramientas(request):
    usuario = request.session.get("usuario")
    mensaje = None
    if usuario:
        mensaje = "Bienvenido a Ferreteria's"

    ruta = Path(__file__).resolve().parent / "data" / "herramientas.json"
    with open(ruta, encoding="utf-8") as f:
        herramientas = json.load(f)

    total = len(herramientas)
    disponibles = sum(1 for h in herramientas if h["stock"] > 0)

    contexto = {
        "herramientas": herramientas,
        "total": total,
        "disponibles": disponibles,
    }
    return render(request, "catalogo/lista.html", contexto)

from django.shortcuts import render, redirect

def login_view(request):
    mensaje = None
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username == "cata" and password == "1234":
            request.session["usuario"] = username
            return redirect("herramientas")
        else:
            mensaje = "Credenciales inválidas"

    return render(request, "catalogo/login.html", {"mensaje": mensaje})


def logout_view(request):
    # Elimina la sesión del usuario
    request.session.flush()
    return redirect("herramientas")  # vuelve al catálogo
