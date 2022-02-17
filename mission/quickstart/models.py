from django.db import models
from django.conf import settings
from django.contrib.auth.models import Group
from rest_framework.authtoken.models import Token

# Create your models here.
class Rights(models.Model):
            
    class Meta:
        
        managed = False  # No database table creation or deletion  \
                         # operations will be performed for this model. 
                
        default_permissions = () # disable "add", "change", "delete"
                                 # and "view" default permissions

        permissions = (
            ("supervision", "peut superviser"),
            ("approbation", "peut faire une approbbation"),
            ("numero", "peut attribuer le numero"),
            ("forfait", "peut changer le forfait"),
            ("validation_rh", "peut validation du drh"),
            ("validation_tg", "peut validation du tg"),
        )

class Pole(models.Model):
    id_pole = models.AutoField(primary_key=True)
    nom_pole = models.CharField(max_length=50)
   

class Entite(models.Model):
    id_entite = models.AutoField(primary_key=True)
    id_pole_id = models.ForeignKey(Pole, on_delete=models.CASCADE)
    nom_entite = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='logo')

class TypeProjet(models.Model):
    id_typeprojet= models.AutoField(primary_key=True)
    nom_typeprojet = models.CharField(max_length=50)


class Projet(models.Model):
    id_projet = models.AutoField(primary_key=True)
    nom_projet= models.CharField(max_length=50)
    date_debut =models.DateTimeField()
    date_fin = models.DateTimeField()
    id_entite= models.ForeignKey(Entite, on_delete=models.CASCADE)
    type_projet = models.ForeignKey(TypeProjet, on_delete=models.CASCADE)

class Processus(models.Model):
    typeprocess = (
        ('N','Normal'),
        ('P','Pôle'),
        ('E','Entité'),
        ('P','Projet'),
        
    )
    id_process = models.AutoField(primary_key=True)
    type_process=models.CharField(max_length=1, choices=typeprocess)
    id_relatated=models.IntegerField()

class Stepprocess(models.Model):
    typesteps = (
        ('i','Initiation'),
        ('V','Validation'),
        ('A','Attribution de numero'),
        ('B','Billet d avion'),
        ('F','Forfait'),
        ('P','Paiement'),
        ('R','Recption du paiement'),
        ('J','Justification de la mission'),
        ('VJ','Validation de la justification'),
        ('VR','Validation du rapport'),

        
    )
    id_stepprocess=models.AutoField(primary_key=True)
    id_process=models.ForeignKey(Processus, on_delete=models.CASCADE)
    cible=models.ForeignKey(Group, on_delete=models.CASCADE)
    type_steps=models.CharField(max_length=2, choices=typesteps)
    order_steps=models.IntegerField()

class Employe(models.Model):
    id_employe = models.AutoField(primary_key=True)
    nom_employe = models.CharField(max_length=50)
    prenoms_employe = models.CharField(max_length=50)
    date_naiss_employe = models.DateField()
    matricule_employe = models.CharField(max_length=50)
    email_employe = models.CharField(max_length=50)
    tel_employe = models.CharField(max_length=50)
    fonction_employe = models.CharField(max_length=100)
    login_employe = models.CharField(max_length=20)
    password_employe = models.CharField(max_length=50)
    compte_actif = models.CharField(max_length=10)
    verrou_employe = models.CharField(max_length=10)
    id_createur = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='createur',on_delete=models.CASCADE)
    id_user = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='user',on_delete=models.CASCADE)
    date_creation = models.DateTimeField()

class Mission(models.Model):
    regime = (
        ('R','Réel'),
        ('F','Forfait'),
        
    )
    avion = (
        ('O','OUI'),
        ('N','NON'),
        
    )
    
    id_mission = models.AutoField(primary_key=True)
    date_demande = models.DateTimeField()   
    objet_mission = models.CharField(max_length=500)
    depart_mission = models.DateField()
    retour_mission = models.DateField()
    lieu_mission = models.CharField(max_length=500)
    statut_mission = models.CharField(max_length=100)
    numero_mission = models.CharField(max_length=20)
    destination_mission = models.CharField(max_length=50)
    contexte_mission = models.CharField(max_length=2000)
    objectifs_mission = models.CharField(max_length=2000)
    frais_extra = models.CharField(max_length=20)
    chg_extra = models.CharField(max_length=20)
    frais_changes = models.CharField(max_length=50)
    current_step = models.IntegerField()
    relance_cible = models.CharField(max_length=50)
    regime=models.CharField(max_length=20, choices=regime)
    type_processus =  models.ForeignKey(Processus, on_delete=models.CASCADE)
    avion=models.CharField(max_length=1, choices=avion)
    id_demandeur=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    

class Envoye(models.Model):
    id_envoye = models.AutoField(primary_key=True)
    id_mission = models.ForeignKey(Mission,related_name='envoye', on_delete=models.CASCADE)
    id_employe = models.ForeignKey(Employe, on_delete=models.CASCADE)
    role = models.CharField(max_length=20)
    billet_avion = models.CharField(max_length=20)
    statut_des_justifs = models.CharField(max_length=20)