from django.views.generic import (ListView, DetailView,CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy
from .models import Cliente

class ClienteListView(ListView):
    model = Cliente
    template_name = 'gestion/cliente_list.html'
    context_object_name = 'clientes'

class ClienteCreateView(CreateView):
    model = Cliente
    fields = ['nombre', 'email', 'telefono', 'rut']
    template_name = 'gestion/cliente_form.html'
    success_url = reverse_lazy('cliente-list')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = ['nombre', 'email', 'telefono', 'rut']
    template_name = 'gestion/cliente_form.html'
    success_url = reverse_lazy('cliente-list')

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'gestion/cliente_confirm_delete.html'
    success_url = reverse_lazy('cliente-list')


