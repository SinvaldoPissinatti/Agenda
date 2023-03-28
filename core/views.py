from django.shortcuts import render, HttpResponse, redirect
from core.models import Evento
# Create your views here.

# def index(request):
#     return redirect('/agenda/')
def local_eventos(request, titulo_evento):
    evento = Evento.objects.get(titulo=titulo_evento)
    mensagem = '<h1>O local do {} é: {}</h1>'.format(titulo_evento, evento.local)
    return HttpResponse (mensagem)

def lista_eventos(request):
    usuario = request.user
    eventos = Evento.objects.all()
    dados = {'eventos' : eventos}
    return render(request, 'agenda.html', dados)