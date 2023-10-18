from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Role(models.Model):
    Name = models.CharField(max_length=20)

    def __str__(self):
        return self.Name


class CustomUser(AbstractUser):
    Telephone = models.CharField(max_length=8, null=True)
    PosteOccupe = models.CharField(max_length=50, choices=[('Architecte Logiciel', 'Architecte Logiciel'),
                                                           ('Analyste Fonctionnel', 'Analyste Fonctionnel'),
                                                           ('Chef de division', 'Chef de division'),
                                                           ('Chef de Mission', 'Chef de Mission'),
                                                           ('Chef de Projet', 'Chef de Projet'),
                                                           ('Développeur', 'Développeur'), (' Testeur', ' Testeur')])
    Grade = models.CharField(max_length=50, choices=[('Ingénieur Principal', 'Ingénieur Principal'),
                                                     ('Ingénieur Major', 'Ingénieur Major'),
                                                     ('Technicien', 'Technicien')])
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True,default=1)



class Reclamation(models.Model):
    Titre = models.CharField(max_length=50)
    Description = models.TextField()
    Date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)

class ReclamationDechiffrer(models.Model):
    Titre = models.CharField(max_length=50)
    Description = models.TextField()
    Date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
