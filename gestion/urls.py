from django.urls import path
from . import views

urlpatterns = [
    path('clientes/', views.ClienteListView.as_view(), name='cliente-list'),
    path('clientes/nuevo/', views.ClienteCreateView.as_view(), name='cliente-create'),
    path('clientes/<int:pk>/editar/', views.ClienteUpdateView.as_view(), name='cliente-update'),
    path('clientes/<int:pk>/eliminar/', views.ClienteDeleteView.as_view(), name='cliente-delete'),
]