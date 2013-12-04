from django.shortcuts import render
from django.shortcuts import render_to_response
from agendapp.models import *

# Create your views here.
def home(request):
	return render_to_response('Home.html', {'Note':Note.objects.all()})

def notas(request):
	return render_to_response('index.html',{'Note':Note.objects.all()})

def horarios(request):
	return render_to_response('Horarios.html',{'Note':Note.objects.all()})

def grupo(request):
	return render_to_response('Grupo.html',{'Note':Note.objects.all()})

def maestro(request):
	return render_to_response('Maestro.html',{'Note':Note.objects.all()})

def aula(request):
	return render_to_response('Aula.html',{'Note':Note.objects.all()})