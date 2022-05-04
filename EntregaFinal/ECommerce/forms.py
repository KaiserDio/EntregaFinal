from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from ECommerce.models import Avatar

class UserEditForm(UserCreationForm):

    email = forms.EmailField(label="Modificar E-mail")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    

    

class Meta:
    model = User
    fields = [ "email", "password1", "password2", "last_name", "first_name"]

    help_text = { k:"" for k in fields }

    permissions = [('ver_cliente', 'Puede Ver Cliente')]
    

class AvatarFormulario(forms.Form):

    avatar = forms.ImageField(required=True)

class Meta:
    model = Avatar
    fields = [ "avatar"]

    help_text = { k:"" for k in fields }

class MensajeFormulario(forms.Form):
    idNovedad = forms.IntegerField()
    idUser = forms.IntegerField()
    profesion = forms.CharField()
    fecha = forms.DateField()