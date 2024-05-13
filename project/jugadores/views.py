from django.shortcuts import render, redirect
from jugadores.models import Jugador
from jugadores.forms import JugadorForm


def index(request):
    return render(request, "jugadores/index.html")

def jugadores_list(request):
    busqueda = request.GET.get("busqueda", None)
    if busqueda:
        print(busqueda)
        consulta = Jugador.objects.filter(nombre__icontains=busqueda)
    else:
        consulta = Jugador.objects.all()   
    
    contexto = {"jugadores": consulta}
    return render(request, "jugadores/jugadores_list.html", contexto)

def jugadores_create(request):
    if request.method == "POST":
        form = JugadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("jugadores:jugadores_list")
    else:  # GET
        form = JugadorForm()
    return render(request, "jugadores/jugadores_create.html", {"form": form})