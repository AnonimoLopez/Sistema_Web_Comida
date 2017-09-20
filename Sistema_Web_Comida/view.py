from django.http import Http404, HttpResponse
from django.template.loader import get_template
from django.template import Context, loader
from django.shortcuts import render
#from django.template.base.Template import *
import datetime
import os.path

def hola(request):
    return HttpResponse("Hola mundo")

def devuelveFecha(request):
    ahora = datetime.datetime.now()
    html = '<HTML><BODY>HORA:%s</body'%ahora
    return HttpResponse(html)

def devuelveHoraAdelanta(request, offset):
    try:
        offset = int(offset)
    except:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render(request, 'hora.html', {'hora': '1'})

    #return HttpResponse(html)



