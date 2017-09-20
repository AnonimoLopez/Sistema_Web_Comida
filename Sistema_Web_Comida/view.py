from django.http import Http404, HttpResponse
import datetime
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
    html = "<html><body>%s - - - %s</body></html>"%(offset, dt)
    return HttpResponse(html)



