from django.shortcuts import render, redirect
from arbitros.models import Arbitro
from arbitros.forms import ArbitroForm

def index(request):
    return render(request, "arbitros/index.html")

def arbitros_list(request):
    busqueda = request.GET.get("busqueda", None)
    if busqueda:
        print(busqueda)
        consulta = Arbitro.objects.filter(nombre__icontains=busqueda)
    else:
        consulta = Arbitro.objects.all()   
    
    contexto = {"arbitros": consulta}
    return render(request, "arbitros/arbitros_list.html", contexto)

def arbitros_create(request):
    if request.method == "POST":
        form = ArbitroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("arbitros:arbitros_list")
    else:  # GET
        form = ArbitroForm()
    return render(request, "arbitros/arbitros_create.html", {"form": form})