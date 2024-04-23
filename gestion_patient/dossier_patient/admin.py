from django.contrib import admin

from .models import Patient
from .models import Praticien
from .models import Centredesanté

# Register your models here.
admin.site.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'age','DateNaissance')

admin.site.register(Praticien)
class PraticienAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom','spécialité','age','DateNaissance')

admin.site.register(Centredesanté)
class CentredesantéAdmin(admin.ModelAdmin):
    list_display = ('nom','lieu','region','district')