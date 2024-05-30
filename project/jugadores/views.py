from django.shortcuts import render, redirect
from jugadores.models import Jugador
from jugadores.forms import JugadorForm
from django.db.models import Q
from django.views.generic import DetailView


def index(request):
    return render(request, "jugadores/index.html")

def jugadores_list(request):
    busqueda = request.GET.get("busqueda", None)
    if busqueda:
        print(busqueda)
        consulta = Jugador.objects.filter(Q(nombre__icontains=busqueda) | Q(apellido__icontains=busqueda))
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
    return render(request, "jugadores/jugadores_form.html", {"form": form})

#class JugadorDetail(DetailView):
#   model = Jugador

def jugadores_detail(request, pk: int):
    consulta = Jugador.objects.get(id=pk)
    contexto = {"jugadores": consulta}
    return render(request, "jugadores/jugadores_detail.html", contexto)


def jugadores_delete(request, pk: int):
    consulta = Jugador.objects.get(id=pk)
    if request.method == "POST":
        consulta.delete()
        return redirect("jugadores:jugadores_list")
    return render(request, "jugadores/jugadores_confirm_delete.html", {"object": consulta})

def jugadores_update(request, pk: int):
    consulta = Jugador.objects.get(id=pk)
    if request.method == "POST":
        form = JugadorForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect("jugadores:jugadores_list")
    else:  # GET
        form = JugadorForm(instance=consulta)
    return render(request, "jugadores/jugadores_form.html", {"form": form})