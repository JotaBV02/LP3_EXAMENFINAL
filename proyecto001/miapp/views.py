from django.shortcuts import render, HttpResponse, redirect

from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Bravo_Persona
from miapp.forms import FormBravoPersona
from django.contrib import messages

# Create your views here.
# Create your views here.
def layout(request):
    estudiantes = [ 'Bravo Veintemilla, Jorge']
    return render(request,'layout.html', {
        'mensaje':'Estudiante',
        'estudiantes': estudiantes
    })

def personas(request):
    return render(request,'personas.html')

def listar_personas(request):
    personas = Bravo_Persona.objects.all();
    return render(request,'listarpersonas.html',{
        'personas': personas,
        'titulo': 'Listado de Personas'
    })

def personas(request):
    if request.method == 'POST':
        formulario = FormBravoPersona(request.POST)
        if formulario.is_valid():
            data_form = formulario.cleaned_data
            # Hay 2 formas de recuperar la información
            #Primera
            nombre  = data_form.get('nombre')
            apellidos  = data_form.get('apellidos')
            #Segunda
            sexo = data_form['sexo']
            #Guardar la informacion
            persona = Bravo_Persona(
                nombre = nombre,
                apellidos = apellidos,
                sexo = sexo,
                
            )
            persona.save()
            
            # Crear un mensaje flash (Sesión que solo se muestra 1 vez)
            messages.success(request, f'Se agregó correctamente a la Persona')
            
            return redirect('listar_personas')
            #return HttpResponse(code + ' -  ' + name + ' - '+ hour + ' - '+ credits + ' - ' + str(state))
    else:
        formulario = FormBravoPersona()
        # Generamos un formulario vacío
    return render(request, 'personas.html',{
        'form': formulario,
        'titulo': 'Agregar Persona'
    })

def eliminar_persona(request, id):
    persona = Bravo_Persona.objects.get(pk=id)
    persona.delete()
    return redirect('listar_personas')