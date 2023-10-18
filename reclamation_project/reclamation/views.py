from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.conf import settings
# Create your views here.
from cryptography.fernet import Fernet, InvalidToken
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .keys import chiffrage_msg, dechiffrage_msg

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
            return redirect('list_reclamation')

    return render(request, 'reclamation/login.html')


@login_required
def create_reclamation(request):
    if request.user.is_authenticated and request.user.role.Name == 'Employee':
        form = ReclamationForm()
        if request.method == 'POST':
            form = ReclamationForm(request.POST)
            if form.is_valid():
                reclamation = form.save(commit=False)
                reclamation.user = request.user
                reclamation.Titre = chiffrage_msg(reclamation.Titre)
                reclamation.Description = chiffrage_msg(reclamation.Description)
                reclamation.save()
        else:
            form = ReclamationForm
        return render(request, 'reclamation/create_reclamation.html',{'form':form})



'''
@login_required
def list_reclamation(request):
    if request.user.is_authenticated and request.user.role.Name == 'Directeur':
        list_reclamations = ReclamationDechiffrer.objects.all()

        print(f"Key directeur :{settings.KEY}")
        for reclamation in list_reclamations:
            try:
                reclamation.Titre = cipher.decrypt(reclamation.Titre).decode()
                reclamation.Description = cipher.decrypt(reclamation.Description).decode()
            except InvalidToken:
                print("Invalid key - Unsuccessfully decrypted")

        return render(request, 'reclamation/directeur_interface.html', {'list_reclamations': list_reclamations})
'''

@login_required
def list_employee_reclamation(request):
    if request.user.is_authenticated and request.user.role.Name == "Employee":
        list_reclamations_employee = Reclamation.objects.filter(user=request.user)

        for reclamation in list_reclamations_employee:
            lenchaine = len(reclamation.Titre)
            print(chiffrage_msg(reclamation.Titre))
            print(dechiffrage_msg(chiffrage_msg(reclamation.Titre)))








        return render(request, 'reclamation/list_employee_reclamation.html', {'listes': list_reclamations_employee})