from multiprocessing import context
from pickle import GET
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import user

# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request): 

    username = request.POST['username']
    password = request.POST['password']

    post = user.objects.all()

    for object in post:

        if(username == object.apellido and password == object.password):
            
            return HttpResponseRedirect(reverse('PagoTrabajadores:calcular_pago'))
        
        else: 
            return HttpResponseRedirect(reverse('PagoTrabajadores:index'))
 
def calcular_pago(request):

    return render(request, 'calcular_pago.html')

def calcular(request):

    horas = float(request.POST['horas'])
    pago = float(request.POST['pago'])

    if(horas > 48):

        context = {

        'pago': request.POST['pago'],
        'horas': request.POST['horas'],
        'horas_extras': float(request.POST['horas']) - 48,
        'pago_final': float(request.POST['pago']) * float(request.POST['horas']) + (float(request.POST['horas']) - 48) * float(request.POST['pago']) * 2 + 50,
        'bonificacion': 50, 
        'pago_hora_extra': float(request.POST['pago'])*2

        }

        return render(request, 'resultados.html', context)
    
    elif(horas <= 48): 

        context = {

        'pago': request.POST['pago'],
        'horas': request.POST['horas'],
        'pago_hora_extra': float(request.POST['pago'])*2,
        'horas_extras': 0,
        'pago_final': float(request.POST['pago']) * float(request.POST['horas']) + 50,
        'bonificacion': 50,

        }
        return render(request, 'resultados.html', context)

    elif(horas < 0 or pago < 0): 

        return HttpResponseRedirect(reverse('PagoTrabajadores:calcular_pago'))

    

def resultados(request):

    return render(request, 'resultados.html')
