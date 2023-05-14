from django import forms
from django.forms import ModelForm
from .models import Produit,Fournisseur,Commande,Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields ="__all__" 
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
class ProfileForm(ModelForm):
        class Meta:
                model = Profile
                fields="__all__"
class ProduitForm(ModelForm): 
        class Meta : 
                model = Produit         
                fields = "__all__" 
                #fields=['libellé','description']
class CommandeForm(forms.ModelForm):
        produits=forms.ModelMultipleChoiceField(
        queryset=Produit.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
        fournisseurs = forms.ModelMultipleChoiceField(
        queryset=Fournisseur.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
        class Meta:
                model = Commande
                fields=['dateCde','produits','fournisseurs']
class FournisseurForm(ModelForm): 
        class Meta : 
                model = Fournisseur         
                fields = "__all__" 
                #fields=['libellé','description']
class UserRegistrationForm(UserCreationForm):
        
        first_name = forms.CharField(label='Prénom')
        last_name = forms.CharField(label='Nom')
        email = forms.EmailField(label='Adresse e-mail')
        
class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name' , 'email')