from django.db import models
from django_cryptography.fields import encrypt
from django.contrib.auth.models import User

# Create your models here.

class Inscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    login_count = encrypt(models.IntegerField(null=True, default=0))
    nom = encrypt(models.CharField(max_length=50))
    prenom = encrypt(models.CharField(max_length=50))
    date_naissance = encrypt(models.DateTimeField(max_length=50))
    mail = encrypt(models.CharField(max_length=50))
    telephone = encrypt(models.CharField(max_length=20))
    adresse = encrypt(models.CharField(max_length=50))
    code_postal = encrypt(models.CharField(max_length=5))
    date_inscription = encrypt(models.DateTimeField(max_length=50))
    fiche_inscription = encrypt(models.ImageField(null=True))
    certificat_medical = encrypt(models.ImageField(null=True))
    date_certificat = encrypt(models.DateTimeField(max_length=50, null=True))
    autorisation_parentale = encrypt(models.ImageField(null=True))
    photo = encrypt(models.ImageField(null=True))
    affiche_trombinoscope = encrypt(models.BooleanField(null=True))
    affiche_annuaire = encrypt(models.BooleanField(null=True))
    cotisation = encrypt(models.BooleanField(null=True))

class Archive(models.Model):
    nom = encrypt(models.CharField(max_length=50))
    prenom = encrypt(models.CharField(max_length=50))
    date_naissance = encrypt(models.DateTimeField(max_length=50))
    mail = encrypt(models.CharField(max_length=50))
    telephone = encrypt(models.CharField(max_length=20))
    adresse = encrypt(models.CharField(max_length=50))
    code_postal = encrypt(models.CharField(max_length=5))
    date_inscription = encrypt(models.DateTimeField(max_length=50))
    fiche_inscription = encrypt(models.ImageField(null=True))
    certificat_medical = encrypt(models.ImageField(null=True))
    date_certificat = encrypt(models.DateTimeField(max_length=50, null=True))
    autorisation_parentale = encrypt(models.ImageField(null=True))
    photo = encrypt(models.ImageField(null=True))
    affiche_trombinoscope = encrypt(models.BooleanField(null=True))
    affiche_annuaire = encrypt(models.BooleanField(null=True))
    date_desinscription = encrypt(models.DateTimeField(max_length=50))
    


    def __str__(self):
            return self.nom

class Categorie(models.Model):
    idAdherent= models.ForeignKey(Inscription,on_delete=models.CASCADE)
    libelle = models.CharField(max_length=50)

    def __str__(self):
        return self.libelle

class Statut(models.Model):
    idAdherent= models.ManyToManyField(Inscription)
    statut = models.CharField(max_length=50)

    def __str__(self):
        return self.statut