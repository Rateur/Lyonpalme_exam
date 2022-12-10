from django import forms

from .models import Inscription

class Formulaire_inscription(forms.Form):#FINIR FORMULAIRE ERREUR POUR L'INSTANT
    nom = forms.CharField(label='Votre nom', max_length=100)
    prenom = forms.CharField(label='Votre prénom', max_length=100)
    #date_naissance = forms.DateField(label='Date naissance')
    mail = forms.CharField(label='Mail', max_length=100)
    telephone = forms.CharField(label='Telephone', max_length=100)
    adresse = forms.CharField(label='Adresse', max_length=100)
    code_postal = forms.CharField(label='Code postal', max_length=100)
    #fiche_inscription = forms.ImageField(label='Fiche inscription')
    #certificat = forms.ImageField(label='Certificat medical')
    #date_certificat = forms.DateField(label='Date certificat')
    #autorisation = forms.ImageField(label='Autorisation parentale')
    #photo = forms.ImageField(label='Photo')