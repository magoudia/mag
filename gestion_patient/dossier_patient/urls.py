from django.urls import path
from . import views


app='dossier_patient'
urlpatterns = [
    path('patients/', views.PatientListView.as_view(), name='listepatient.html'),
    path('praticiens/', views.PraticienListView.as_view(), name='listepraticiens.html'),
    path('centres/', views.CentredesantéListView.as_view(), name='listecentresanté.hml'),
    path('',views.home,name='index.html')
    
]