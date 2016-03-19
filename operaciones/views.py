from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def suma(request, uno, dos):
    respuesta = 'Sumamos:' + str(uno) + "+" + str(dos)
    respuesta += "=" + str(int(uno)+int(dos))
    return HttpResponse (respuesta)

def resta(request, uno, dos):
    respuesta = 'Restamos:' + str(uno) + "-" + str(dos)
    respuesta += "=" + str(int(uno)-int(dos))
    return HttpResponse (respuesta)

def multiplicacion(request, uno, dos):
    respuesta = 'Multiplicamos:' + str(uno) + "*" + str(dos)
    respuesta += "=" + str(int(uno)*int(dos))
    return HttpResponse (respuesta)

def division(request, uno, dos):
    respuesta = 'Dividimos:' + str(uno) + "/" + str(dos)
    respuesta += "=" + str(int(uno)/int(dos))
    return HttpResponse (respuesta)

def explicacion(request):
    respuesta = "oper1+oper2<br/>" + "oper1-oper2<br/>"
    respuesta += "oper1*oper2<br/>" + "oper1/oper2<br/>"
    return HttpResponse(respuesta)
def notFound(request):
    return HttpResponse("Not Found")
