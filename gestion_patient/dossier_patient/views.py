from django.shortcuts import render
from .models import Patient
from .models import Praticien
from .models import Centredesanté

# Create your views here.
from django.views.generic import ListView

class PatientListView(ListView):
    model = Patient
    template_name = 'listepatient.html'  # Nom du template HTML pour afficher la liste des cours
    context_object_name = 'patients'  # Nom de la variable de contexte dans le template

class PraticienListView(ListView):
    model = Praticien
    template_name = 'listepraticiens.html'  # Nom du template HTML pour afficher la liste des étudiants
    context_object_name = 'praticiens'  # Nom de la variable de contexte dans le template
class CentredesantéListView(ListView):
    model = Centredesanté
    template_name = 'listecentresanté.html'  # Nom du template HTML pour afficher la liste des étudiants
    context_object_name = 'centres'  # Nom de la variable de contexte dans le template

def home (request):
    return render(request, 'index.html')



