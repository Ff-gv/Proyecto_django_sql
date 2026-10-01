from django import forms
from .models import Cliente,Cuenta,Transaccion

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre',
                'apellido',
                'correo',
                'telefono_celular',
                'direccion',
                ]
        widgets = {
            'nombre':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su nombre',
            }
            ),
            'correo':forms.EmailInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese e-mail'
                }
            ),
            'apellido':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su apellido'
                }
            ),
            'telefono_celular':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su numero celular'
                }
            ),
            'direccion':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su direccion'
                }
            )
            
                }
class CuentaForm(forms.ModelForm):
    class Meta:
        model = Cuenta
        fields = [
            'cliente',
            'n_cuenta',
            'saldo',
            'tipo_cuenta',
        ]
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-select'}),
            'n_cuenta': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese numero de cuenta'}),
            'saldo': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0.00'}),
            'tipo_cuenta': forms.Select(attrs={'class': 'form-select'}),
            }
class TransaccionForm(forms.ModelForm):
    class Meta:
        model = Transaccion
        fields = [
            'cuenta',
            'monto',
            'descripcion',
            'tipo_transaccion',
        ]
        widgets = {
            'cuenta': forms.Select(attrs={'class':'form-select'}),
            'monto': forms.NumberInput(attrs={'class':'form-control','placeholder':'Ingrese monto'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control', 'rows': 2}),
            'tipo_transaccion': forms.Select(attrs={'class':'form-select'})
        }
        