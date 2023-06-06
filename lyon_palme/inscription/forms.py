from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import Inscription

class Formulaire_inscription(forms.Form):
    nom = forms.CharField(label='Nom', max_length=100)
    prenom = forms.CharField(label='Prénom', max_length=100)
    mail = forms.CharField(label='Mail', max_length=100)
    telephone = forms.CharField(label='Téléphone', max_length=100)
    adresse = forms.CharField(label='Adresse', max_length=100)
    code_postal = forms.CharField(label='Code postal', max_length=100)
    #fiche_inscription = forms.ImageField(label='Fiche inscription')
    #certificat = forms.ImageField(label='Certificat medical')
    #autorisation = forms.ImageField(label='Autorisation parentale')
    #photo = forms.ImageField(label='Photo')

class LoginForm(AuthenticationForm):
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)