import django.views.generic
from django.shortcuts import render
from datetime import datetime
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import DetailView
from django.views.generic.list import ListView
from cars.models import *
from django.urls import reverse_lazy



class Index(TemplateView):
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