from django.db import models

# Create your models here.
class Inscription(models.Model):
    nom = models.CharField(max_length=50, help_text='Rentrez votre nom')
    prenom = models.CharField(max_length=50, help_text='Rentrez votre prénom')
    date_naissance = models.DateTimeField(max_length=50, help_text='Rentrez votre date de naissance')
    mail = models.CharField(max_length=50, help_text='Rentrez votre adresse email')
    telephone = models.CharField(max_length=20, help_text='Rentrez votre numéro de téléphone')
    adresse = models.CharField(max_length=50, help_text='Rentrez votre adresse')
    code_postal = models.IntegerField(max_length=50, help_text='Rentrez votre code postal')
    date_inscription = models.DateTimeField(max_length=50)
    fiche_inscription = models.BinaryField(max_length=50)
    certificat_medical = models.BinaryField(max_length=50, help_text='Ajoutez votre certificat médical')
    date_certificat = models.DateTimeField(max_length=50)
    autorisation_parentale = models.BinaryField(max_length=50)
    photo = models.BinaryField(max_length=50)
    

#class Choice(models.Model):
 #   question = models.ForeignKey(Question, on_delete=models.CASCADE)
  #  choice_text = models.CharField(max_length=200)
   # votes = models.IntegerField(default=0)