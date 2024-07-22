from django import forms
from django.core import validators

class FormBravoPersona(forms.Form):

    nombre = forms.CharField(
        label="Nombre de la Persona",
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingrese el Nombre de la Persona',
            }
        ),
        validators=[
            validators.RegexValidator('^[A-Za-z0-9nÑ ]*$','El nombre tiene caracteres inválidos','name_invalido')            
        ] 
    )
    
    apellidos = forms.CharField(
        label = "Apellidos de la Persona",
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingrese los Apellidos de la Persona',
            }
        ),
        validators=[
            validators.RegexValidator('^[A-Za-z0-9nÑ ]*$','Los apellidos tiene caracteres inválidos','name_invalido')            
        ]
    )
       
    opciones_sexo = [
        (1, 'Masculino'),
        (0, 'Femenino'),
    ]
    sexo = forms.TypedChoiceField(
        label = "¿Sexo?",
        required=True,
        choices = opciones_sexo
    )
