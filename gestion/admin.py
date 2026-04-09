from django.contrib import admin
from .models import Cliente, Cuenta, Transaccion

from django.contrib import admin
from .models import Cliente, Cuenta, Transaccion

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'rut', 'creado_en')
    search_fields = ('nombre', 'rut')

@admin.register(Cuenta)
class CuentaAdmin(admin.ModelAdmin):
    list_display = ('numero', 'cliente', 'tipo', 'saldo', 'activa')
    list_filter = ('tipo', 'activa')

@admin.register(Transaccion)
class TransaccionAdmin(admin.ModelAdmin):
    # Esto permite ver los datos clave en la lista principal del admin
    list_display = ('id', 'tipo', 'cuenta_origen', 'cuenta_destino', 'monto', 'fecha')
    
    # Permite filtrar por tipo de movimiento o fecha en el panel lateral
    list_filter = ('tipo', 'fecha')
    
    # Permite buscar transacciones por el número de cuenta
    search_fields = ('cuenta_origen__numero', 'cuenta_destino__numero', 'descripcion')
    
    # Hace que la fecha sea de solo lectura para evitar alteraciones manuales
    readonly_fields = ('fecha',)