from django.contrib.auth.models import User, Group
from rest_framework import serializers
from quickstart.models import Mission,Envoye,Employe,Processus,Stepprocess,Pole,Entite,TypeProjet,Projet





class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']



class EnvoyeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Envoye
        fields = ['id_envoye', 'id_mission', 'id_employe','role','billet_avion','statut_des_justifs']

class StepprocessSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stepprocess
        fields = ['id_stepprocess','cible','type_steps','order_steps']

class ProcessusSerializer(serializers.HyperlinkedModelSerializer):
    Stepprocess = StepprocessSerializer(many=True, read_only=True)
    class Meta:
        model = Processus
        fields = ['id_process','type_process','id_relatated','Stepprocess']


class MissiontSerializer(serializers.HyperlinkedModelSerializer):
    envoye = EnvoyeSerializer(many=True, read_only=True)
    process = ProcessusSerializer(many=True, read_only=True)
        
    class Meta:
        model = Mission
        fields = ['id_mission', 'date_demande', 'objet_mission', 'depart_mission', 'retour_mission', 'lieu_mission','statut_mission','numero_mission','destination_mission','contexte_mission','objectifs_mission','frais_extra','chg_extra','current_step','relance_cible','process','envoye']


class UserSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups','mission']

class EmployeSerializer(serializers.ModelSerializer):
    envoye = EnvoyeSerializer(many=True, read_only=True)
    class Meta:
        model = Employe
        fields = ['envoye','id_employe', 'nom_employe', 'prenoms_employe','date_naiss_employe','email_employe','tel_employe','fonction_employe','login_employe','password_employe','compte_actif','verrou_employe','id_createur','id_user','date_creation']

class User1Serializer(serializers.ModelSerializer):
    mission = MissiontSerializer(many=True, read_only=True)
    employe = EmployeSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups','mission','employe','employe']

class PoleSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Pole
        fields = ['id_pole', 'nom_pole']

class EntiteSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Entite
        fields = ['id_entite', 'id_pole_id','nom_entite','logo']

class TypeProjetSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = TypeProjet
        fields = ['id_typeprojet', 'nom_typeprojet']

class ProjetSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Projet
        fields = ['id_projet', 'nom_projet','date_debut','date_fin','id_entite','type_projet']





