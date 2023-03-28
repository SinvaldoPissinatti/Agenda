from django.shortcuts import render, HttpResponse
from core.models import Evento
# Create your views here.
def local_eventos(request, titulo_evento):
    evento = Evento.objects.get(titulo=titulo_evento)
    mensagem = '<h1>O local do {} é: {}</h1>'.format(titulo_evento, evento.local)
    return HttpResponse (mensagem)