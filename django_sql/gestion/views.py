from django.shortcuts import render

from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Cliente,Cuenta,Transaccion
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ClienteForm, CuentaForm, TransaccionForm
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.

class ClienteListView(LoginRequiredMixin,ListView):
    model = Cliente
    template_name = 'gestion/cliente_list.html'
    context_object_name = 'clientes'
    #cuando llame a mi iteracion en etiquetas for, esto es lo que debo usar, la palabra clientes
class ClienteCreateView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'gestion/cliente_form.html'
    success_url = reverse_lazy('cliente_list')
    success_message = "Cliente registrado con exito."
class ClienteUpdateView(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'gestion/cliente_form.html'
    success_url = reverse_lazy('cliente_list')
    success_message = "Los datos del cliente se actualizaron correctamente."
class ClienteDeleteView(LoginRequiredMixin,SuccessMessageMixin,DeleteView):
    model = Cliente
    template_name = 'gestion/cliente_delete.html'
    success_url = reverse_lazy('cliente_list')
    success_message = "El cliente ha sido eliminado de la base de datos."

    
class CuentaListView(LoginRequiredMixin,ListView):
    model = Cuenta
    template_name = 'gestion/cuenta_list.html'
    context_object_name = 'cuentas'
class CuentaCreateView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model = Cuenta
    form_class = CuentaForm
    template_name = 'gestion/cuenta_form.html'
    success_url = reverse_lazy('cuenta_list')
    success_message = "Cuenta registrada con exito."
class CuentaUpdateView(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    model = Cuenta
    form_class = CuentaForm
    template_name = 'gestion/cuenta_form.html'
    success_url = reverse_lazy('cuenta_list')
    success_message = "Los datos del la cuenta se actualizaron correctamente."
class CuentaDeleteView(LoginRequiredMixin,SuccessMessageMixin,DeleteView):
    model = Cuenta
    template_name = 'gestion/cuenta_delete.html'
    success_url = reverse_lazy('cuenta_list')
    success_message = "La cuenta ha sido eliminada de la base de datos."

class TransaccionListView(LoginRequiredMixin,ListView):
    model = Transaccion
    template_name = 'gestion/transaccion_list.html'
    context_object_name = 'transacciones'
class TransaccionCreateView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model = Transaccion
    form_class = TransaccionForm
    template_name = 'gestion/transaccion_form.html'
    success_url = reverse_lazy('transaccion_list')
    success_message = "transaccion registrada con exito."
class TransaccionUpdateView(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    model = Transaccion
    form_class = TransaccionForm
    template_name = 'gestion/transaccion_form.html'
    success_url = reverse_lazy('transaccion_list')
    success_message = "Los datos del la transaccion se actualizaron correctamente."
class TransaccionDeleteView(LoginRequiredMixin,SuccessMessageMixin,DeleteView):
    model = Transaccion
    template_name = 'gestion/transaccion_delete.html'
    success_url = reverse_lazy('transaccion_list')
    success_message = "La transacción ha sido eliminada de la base de datos."

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