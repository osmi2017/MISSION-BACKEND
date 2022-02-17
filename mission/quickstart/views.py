from django.contrib.auth.models import User, Group
from quickstart.models import Employe, Envoye, Mission,Employe,Stepprocess,Processus,Pole,Entite,TypeProjet,Projet
from rest_framework import viewsets
from rest_framework import permissions
from quickstart.serializers import UserSerializer, GroupSerializer,MissiontSerializer,ProcessusSerializer,StepprocessSerializer,User1Serializer,EmployeSerializer,PoleSerializer,TypeProjetSerializer,EntiteSerializer,ProjetSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework import generics
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.renderers import JSONRenderer


from django.contrib.auth.models import Permission


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data,
                                            context={'request': request})
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
        
            token, created = Token.objects.get_or_create(user=user)
        
            return Response({
                    'token': token.key,
                    'user_id': user.pk,
                    'email': user.email,
                    'username':user.username,
                    'name':user.first_name,
                    'lastname':user.last_name

            })
        except:
            return JsonResponse({'error':'Login ou mot de passe incorrecte'})


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]




class MesMissionList(APIView):
    """
    Liste de mes missions, or create a new mission.
    """
    #permission_classes = [permissions.IsAuthenticated]
    def get(self, request, id=id,format=None):
        employe=Employe.objects.filter(id_user=id).values('id_employe')
        
        envoye=Envoye.objects.filter(id_employe__in= employe).values('id_envoye')
        print(envoye)
        mission = Mission.objects.filter(envoye__id_envoye__in=envoye).distinct()
        serializer = MissiontSerializer(mission,context={'request': request}, many=True)
        return Response(serializer.data)
        # if data:
        #     for mission in serializer.data:
        #         name = mission.pop("id_mission")
        #         modified_response[name] = mission
        # return Response(modified_response)

    def post(self, request, format=None):
        serializer = MissiontSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MesMissionDetail(APIView):
    """
    Retrieve, update or delete a mission instance.
    """
    #permission_classes = [permissions.IsAuthenticated]
    def get_object(self, pk):
        try:
            return Mission.objects.get(pk=pk)
        except Mission.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        mission = self.get_object(pk)
        serializer = MissiontSerializer(mission)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        mission = self.get_object(pk)
        serializer = MissiontSerializer(mission, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        mission = self.get_object(pk)
        mission.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProcessList(generics.ListCreateAPIView):
    queryset = Processus.objects.all()
    serializer_class = ProcessusSerializer


class ProcessDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Processus.objects.all()
    serializer_class =  ProcessusSerializer

class StepprocessList(generics.ListCreateAPIView):
    queryset = Stepprocess.objects.all()
    serializer_class = StepprocessSerializer


class StepprocessDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stepprocess.objects.all()
    serializer_class =  StepprocessSerializer

class userList(generics.ListCreateAPIView):
     queryset = User.objects.all()
     serializer_class = User1Serializer

class userDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class =  User1Serializer


class employeList(generics.ListCreateAPIView):
     queryset = Employe.objects.all()
     serializer_class = EmployeSerializer

class employeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employe.objects.all()
    serializer_class =  EmployeSerializer

class poleList(generics.ListCreateAPIView):
     queryset = Pole.objects.all()
     serializer_class = PoleSerializer

class poleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pole.objects.all()
    serializer_class =  PoleSerializer

class entiteList(generics.ListCreateAPIView):
     queryset = Entite.objects.all()
     serializer_class = EntiteSerializer

class entiteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Entite.objects.all()
    serializer_class =  EntiteSerializer

class typeprojetList(generics.ListCreateAPIView):
     queryset = TypeProjet.objects.all()
     serializer_class = TypeProjetSerializer

class typeprojetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TypeProjet.objects.all()
    serializer_class =  TypeProjetSerializer

class projetList(generics.ListCreateAPIView):
     queryset = Projet.objects.all()
     serializer_class = ProjetSerializer

class projetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Projet.objects.all()
    serializer_class =  ProjetSerializer



