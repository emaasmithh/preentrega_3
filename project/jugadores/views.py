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
    return render(request, "jugadores/jugadores_create.html", {"form": form})

#class JugadorDetail(DetailView):
#   model = Jugador

def jugadores_detail(request, pk: int):
    consulta = Jugador.objects.get(id=pk)
    contexto = {"jugadores": consulta}
    return render(request, "jugadores/jugadores_detail.html", contexto)