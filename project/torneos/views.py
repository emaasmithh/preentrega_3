from django.shortcuts import render, redirect
from torneos.models import Torneo
from torneos.forms import TorneoForm


def index(request):
    return render(request, "torneos/index.html")

def torneos_list(request):
    busqueda = request.GET.get("busqueda", None)
    if busqueda:
        print(busqueda)
        consulta = Torneo.objects.filter(nombre__icontains=busqueda)
    else:
        consulta = Torneo.objects.all()   
    
    contexto = {"torneos": consulta}
    return render(request, "torneos/torneos_list.html", contexto)

def torneos_create(request):
    if request.method == "POST":
        form = TorneoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("torneos:torneos_list")
    else:  # GET
        form = TorneoForm()
    return render(request, "torneos/torneos_create.html", {"form": form})