from django import forms

import inscription

class Formulaire_inscription(forms.ModelForm):#FINIR FORMULAIRE ERREUR POUR L'INSTANT
    model = Inscription
    fields = '__all__'