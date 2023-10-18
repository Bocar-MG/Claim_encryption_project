from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Reclamation, CustomUser, Role, ReclamationDechiffrer


# Register your models here.

@admin.register(Reclamation)
class ReclamationAdmin(admin.ModelAdmin):
    list_display = ("Titre", "Description","Date")


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name","PosteOccupe","Grade")

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('Name',)


