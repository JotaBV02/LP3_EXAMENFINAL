from django.shortcuts import render, HttpResponse, redirect

from django.shortcuts import render

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