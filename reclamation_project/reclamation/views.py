from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.conf import settings
# Create your views here.
from cryptography.fernet import Fernet, InvalidToken
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .keys import chiffrage_msg, dechiffrage_msg, encrypt, decrypt

from .forms import ReclamationForm, CustomUserRegistrationForm, AuthenticationUserForm, ReclamationDechiffrerForm

from .models import Reclamation, ReclamationDechiffrer


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('connexion')
    else:
        form = CustomUserRegistrationForm()
    return render(request, 'reclamation/registration.html', {'form': form})


def connexion(request):
    if request.method == "POST":
        print("Good form")
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        print("Good authenticate")
        if user.role.Name == 'Employee':
            login(request, user)
            return redirect('create_claim')
        elif user.role.Name == 'Directeur':
            login(request, user)
            return redirect('list_claim')

    return render(request, 'reclamation/login.html')


@login_required
def create_reclamation(request):
    if request.user.is_authenticated and request.user.role.Name == 'Employee':
        formulaire = ReclamationForm()
        if request.method == 'POST':
            formulaire = ReclamationForm(request.POST)
            if formulaire.is_valid():
                reclamation = formulaire.save(commit=False)
                reclamation.user = request.user
                #reclamation.Titre = chiffrage_msg(reclamation.Titre)
                #reclamation.Description = chiffrage_msg(reclamation.Description)
                reclamation.Titre = encrypt(reclamation.Titre)
                reclamation.Description = encrypt(reclamation.Description)
                reclamation.save()
                return redirect('liste')
        else:
            formulaire = ReclamationForm
        return render(request, 'reclamation/create_reclamation.html', {'formulaire': formulaire})



@login_required
def list_reclamation(request):
    if request.user.is_authenticated and request.user.role.Name == 'Directeur':
        list_reclamations = Reclamation.objects.all()
        for reclamation in list_reclamations:
            try:
                # Decryptage des donnees cryptees depuis la base de donneés coté Directeur
                reclamation.Titre = decrypt(reclamation.Titre)
                reclamation.Description = decrypt(reclamation.Description)
            except InvalidToken:
                print("Invalid key - Unsuccessfully decrypted")

        return render(request, 'reclamation/responsable_reclamation.html', {'list_reclamations': list_reclamations})



@login_required
def list_employee_reclamation(request):
    if request.user.is_authenticated and request.user.role.Name == "Employee":
        list_reclamations_employee = Reclamation.objects.filter(user=request.user)
        for reclamation in list_reclamations_employee:
            reclamation.Titre = decrypt(reclamation.Titre)
            reclamation.Description = decrypt(reclamation.Description)
        return render(request, 'reclamation/list_employee_reclamation.html', {'listes': list_reclamations_employee})

@login_required
def Deconnexion(request):
    logout(request)
    return redirect('register')