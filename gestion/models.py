from django.db import models
from django.contrib.auth.models import User


# Definición de modelos Cliente, Cuenta, Transacción

class Cliente(models.Model):
    """Perfil extendido de un usuario de la billetera."""

    usuario   = models.OneToOneField(User, on_delete=models.CASCADE)  # 1-a-1
    nombre    = models.CharField(max_length=100)
    email     = models.EmailField(unique=True)
    telefono  = models.CharField(max_length=20, blank=True, null=True)
    rut       = models.CharField(max_length=20, unique=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['nombre']


class Cuenta(models.Model):
    """Cuenta digital asociada a un cliente."""
    TIPO_CHOICES = [
        ('ahorro',   'Cuenta de Ahorro'),
        ('corriente','Cuenta Corriente'),
    ]
    cliente    = models.ForeignKey(            # Muchos-a-Uno
        Cliente, on_delete=models.CASCADE,
        related_name='cuentas'
    )
    numero     = models.CharField(max_length=20, unique=True)
    tipo       = models.CharField(max_length=20, choices=TIPO_CHOICES, default='ahorro')
    saldo      = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    activa     = models.BooleanField(default=True)
    creada_en  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.numero} ({self.tipo})'

class Transaccion(models.Model):
    """Movimiento de fondos entre cuentas."""
    TIPO_CHOICES = [
        ('deposito',    'Depósito'),
        ('retiro',      'Retiro'),
        ('transferencia','Transferencia'),
    ]
    cuenta_origen  = models.ForeignKey(
        Cuenta, on_delete=models.PROTECT,
        related_name='transacciones_origen'
    )
    cuenta_destino = models.ForeignKey(
        Cuenta, on_delete=models.PROTECT,
        related_name='transacciones_destino',
        null=True, blank=True  # null en depósitos/retiros
    )
    tipo       = models.CharField(max_length=20, choices=TIPO_CHOICES)
    monto      = models.DecimalField(max_digits=12, decimal_places=2)
    descripcion= models.TextField(blank=True)
    fecha      = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.tipo} - ${self.monto} ({self.fecha:%d/%m/%Y})'

