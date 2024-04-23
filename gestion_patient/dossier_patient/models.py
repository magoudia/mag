from django.db import models

# Create your models here.
class Patient(models.Model):
   nom= models.CharField(max_length=255)
   prenom = models.CharField(max_length=255)
   age = models.IntegerField()
   DateNaissance=models.DateField()
  
class Praticien(models.Model):
   nom = models.CharField(max_length=100)
   prenom= models.CharField(max_length=300)
   age = models.IntegerField()
   DateNaissance=models.DateField()
   spécialité=models.CharField(max_length=300)
   
class Centredesanté(models.Model):
    nom=models.CharField(max_length=100)
    lieu=models.CharField(max_length=200)
    region=models.CharField(max_length=150)
    district=models.CharField(max_length=50)
    

