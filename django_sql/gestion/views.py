from django.shortcuts import render

from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Cliente
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ClienteForm
# Create your views here.

class ClienteListView(LoginRequiredMixin,ListView):
    model = Cliente
    template_name = 'gestion/cliente_list.html'
    context_object_name = 'clientes'
    #cuando llame a mi iteracion en etiquetas for, esto es lo que debo usar, la palabra clientes
class ClienteCreateView(LoginRequiredMixin,CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'gestion/cliente_form.html'
    success_url = reverse_lazy('cliente_list')
class ClienteUpdateView(LoginRequiredMixin,UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'gestion/cliente_form.html'
    success_url = reverse_lazy('cliente_list')
class ClienteDeleteView(LoginRequiredMixin,DeleteView):
    model = Cliente
    template_name = 'gestion/cliente_delete.html'
    success_url = reverse_lazy('cliente_list')

#Esto es una alternativa si no ocupo form, crear los campos directamente en mis vistas
    # class ClienteCreateView(CreateView):
#     model = Cliente
#     fields = [
#         'nombre',
#         'apellido',
#         'correo',
#         'telefono_celular',
#         'direccion',
#     ]
#     template_name = 'gestion/cliente_form.html'
#     success_url = reverse_lazy('cliente_list')

# #hacer un cliente  update es lo mismo que hacer un cliente create
# class ClienteUpdateView(UpdateView):
#     model = Cliente
#     fields = [
#         'nombre',
#         'apellido',
#         'correo',
#         'telefono_celular',
#         'direccion',
#         ]
#     template_name = 'gestion/cliente_form.html'
#     success_url = reverse_lazy('cliente_list')