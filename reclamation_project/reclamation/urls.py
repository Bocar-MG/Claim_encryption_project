"""
URL configuration for app_claim project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path


from .views import register, create_reclamation, connexion, list_employee_reclamation, Deconnexion, list_reclamation

urlpatterns = [
    path('', register, name='register'),
    path('connexion/', connexion, name='connexion'),
    path('create_claim/', create_reclamation, name='create_claim'),
    path('deconnexion/',Deconnexion,name='deconnexion'),
    path('liste/',list_employee_reclamation,name='liste'),
    path('list_claim/',list_reclamation,name='list_claim')
]

