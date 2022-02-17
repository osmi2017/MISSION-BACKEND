"""mission URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from quickstart import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views as authview

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-auth/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('mes-missionlist/<int:id>/', views.MesMissionList.as_view()),
    path('mes-missiondetail/<int:pk>/', views.MesMissionDetail.as_view()),
    path('processlist', views. ProcessList.as_view()),
    path('processlist/<int:pk>/', views.ProcessDetail.as_view()),
    path('Stepprocess', views. StepprocessList.as_view()),
    path('Stepprocess/<int:pk>/', views.StepprocessDetail.as_view()),
    path('userlist/<int:id>/', views.userList.as_view()),
    path('userdetail/<int:pk>/', views.userDetail.as_view()),
    path('Employelist/', views.employeList.as_view()),
    path('Employedetail/', views.employeDetail.as_view()),
    path('polelist/', views.poleList.as_view()),
    path('poledetail/', views.poleDetail.as_view()),
    path('entitelist/', views.entiteList.as_view()),
    path('entitedetail/', views.entiteDetail.as_view()),
    path('projetlist/', views.projetList.as_view()),
    path('projetdetail/', views.projetDetail.as_view()),
    path('typeprojetlist/', views.typeprojetList.as_view()),
    path('typrojetdetail/', views.typeprojetDetail.as_view()),
    path('authentification', views.StepprocessDetail.as_view()),
    path('api-token-auth/', views.CustomAuthToken.as_view()),
]


