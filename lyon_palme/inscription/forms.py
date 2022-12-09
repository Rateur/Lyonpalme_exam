from django import forms

import inscription

class Formulaire_inscription(forms.ModelForm):#FINIR FORMULAIRE ERREUR POUR L'INSTANT
    model = inscription
    fields = '__all__'