from django import forms
from .models import Cliente

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
            'telefono':forms.TextInput(
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