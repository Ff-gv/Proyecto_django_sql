from django.contrib import admin
from .models import Cliente,Cuenta,Transaccion,Promocion,Descripcion
# Register your models here.
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'apellido',
        'correo',
        'telefono_celular',
        'direccion',
    )
    search_fields = (
        'nombre',
        'apellido',
        'correo'
    )
@admin.register(Cuenta)
class CuentaAdmin(admin.ModelAdmin):
    list_display = (
        'saldo',
        'tipo_cuenta',
        'n_cuenta',
        'cliente',
    )
    list_filter = (
        'tipo_cuenta',            
        )
@admin.register(Transaccion)
class TransaccionAdmin(admin.ModelAdmin):
    list_display = (
        'tipo_transaccion',
        'monto',
        'cuenta',
        'descripcion',
    )
    list_filter = (
        'tipo_transaccion',    
        )
@admin.register(Promocion)
class PromocionAdmin(admin.ModelAdmin):    
    list_display = (
        'nombre',
        'descuento'
    )
@admin.register(Descripcion)
class DescripcionAdmin(admin.ModelAdmin):
    list_display = (
        'cliente',
        'pelo',
    )   