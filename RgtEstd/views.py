from django.views.generic import TemplateView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from RgtEstd.models import *
from django.urls import reverse_lazy
from RgtEstd.archivos.archivos import *
from django.shortcuts import render, redirect



class Index_P(TemplateView):
    template_name = "index.html"

class Formulario1(CreateView):
    model = Formulario
    fields = ['usuario', 'nombre', 'password','password2','correo','telefono']
    template_name = "formulario.html"
    success_url = reverse_lazy("index")

class ListaF(ListView):
    model = Formulario
    template_name = "lista.html"

class ModificarF(UpdateView):
    model = Formulario
    fields = [ 'nombre', 'password','password2','correo','telefono','usuario']
    template_name = "consulta.html"
    success_url = reverse_lazy("index")

class DeleteR(DeleteView):
    model = Formulario
    template_name = "eliminar.html"
    success_url = reverse_lazy("index")

def index(request):
    template = "index.html"
    context = {}
    return render(request,template,context)

def login(request):
    ruta = "C:/Users/Alex y Luis/PycharmProjects/Mafko/datos.txt"
    usu = request.POST.get('user')
    pas = request.POST.get('password')
    print(usu,pas)
    arch = Archivo()
    obj = arch.getLogin(usu,pas,ruta)
    print(ruta,obj)
    if obj==None:
        return render(request, "login.html")
    else:
        if obj.usuario == usu :
            return render(request, "index.html")

