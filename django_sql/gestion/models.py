from django.db import models


# Create your models here.
class Promocion(models.Model):
    nombre = models.CharField(max_length=100)
    descuento = models.IntegerField()

    def __str__(self):
        return self.nombre
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    correo = models.EmailField(max_length=70,unique=True)
    telefono_celular = models.CharField(max_length=35,blank=True,null=True)
    direccion = models.CharField(max_length=200)
    fecha_inscripcion = models.DateField(auto_now_add=True)
    promocion = models.ManyToManyField(Promocion, blank=True, related_name='clientes')
    def __str__(self):
        return f'{self.nombre}-{self.apellido}'
    
class Descripcion(models.Model):
    TIPO_CHOICES = [
        ('NEGRO','negro'),
        ('RUBIO','rubio'),
        ('CAFE','cafe'),
        ('OTRO','otro'),
    ]
    cliente = models.OneToOneField(Cliente,on_delete=models.CASCADE)
    pelo = models.CharField(max_length=50, choices=TIPO_CHOICES)

class Cuenta(models.Model):
#esto es una tupla o lista, recordar
    TIPO_CHOICES = [
        ('CUENTA_AHORRO','cuenta ahorro'),
        ('CUENTA_CORRIENTE','cuenta corriente'),
        ('CUENTA_VISTA','cuenta vista')               
                    ]
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE,related_name='cuentas')
    n_cuenta = models.CharField(max_length=50,unique=True)
    saldo = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    tipo_cuenta = models.CharField(max_length=25,choices=TIPO_CHOICES)
    def __str__(self):
        return f'{self.cliente.nombre}-{self.n_cuenta}'
class Transaccion(models.Model):
    TIPO_CHOICES = [
        ('TRANSFERENCIA','transferencia'),
        ('RETIRO','retiro'),
        ('DEPOSITO','deposito')

    ]
    cuenta = models.ForeignKey(Cuenta,on_delete=models.PROTECT,related_name='transacciones')
    monto = models.DecimalField(max_digits=10,decimal_places=2)
    fecha = models.DateTimeField(auto_now_add = True)
    descripcion = models.TextField(max_length=300,null=True,blank=True)
    tipo_transaccion = models.CharField(max_length=35,choices=TIPO_CHOICES)


#si me sale esto: It is impossible to add the field 'fecha_creacion' with 'auto_now_add=True' to cuenta without providing a default. This is because the database needs something to populate existing rows.
#  1) Provide a one-off default now which will be set on all existing rows
#  2) Quit and manually define a default value in models.py.
#es mejor escribir None para pasar las advertencias y continuar con mi base de datos, selecciona 1 y escribe None
#si sale fechas usa si o si timezone.now y mandarle enter 