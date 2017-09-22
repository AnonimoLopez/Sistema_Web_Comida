from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.template import RequestContext
def inicio(request):
    return HttpResponse('Hola',context_instance=RequestContext(request))


# Create your views here.
