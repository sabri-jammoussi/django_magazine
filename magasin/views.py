# from django.shortcuts import render
# from django.template import loader
# from .models import Produit
# def index(request):
#     products= Produit.objects.all()
#     context={'products':products}
#     return render( request,'magasin/mesProduits.html ',context )
#pour l'affichage lowel 
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.template import loader
from .models import Produit,Commande
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .models import Produit
from .forms import ProduitForm,FournisseurForm,CommandeForm,UserUpdateForm, ProfileUpdateForm
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .models import Fournisseur
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

# def index(request):
#      list=Produit.objects.all()
#      return render(request,'magasin/vitrine.html',{'list':list})
# #pour l'affichage lowel
##hethom CRUD lil Fournisseur
def edit_fournisseur(request, id):
    post = get_object_or_404(Fournisseur, id=id)

    if request.method == 'GET':
        context = {'form': FournisseurForm(instance=post), 'id': id}
        return render(request,'magasin/fournisseur/editfournisseur.html',context)
    elif request.method == 'POST':
         form = FournisseurForm(request.POST, instance=post)
         if form.is_valid():
              form.save()
              messages.success(request, 'The post has been updated successfully.')
              return redirect('/magasin/nouvFournisseur/')
         else:
            messages.error(request, 'Please correct the following errors:')
            return render(request,'magasin/fournisseur/editfournisseur.html',{'form':form})
       ###########################################
def delete_fournisseur(request, id):
    post = get_object_or_404(Fournisseur, id=id)
    context = {'post': post}    
    
    if request.method == 'GET':
        return render(request, 'magasin/fournisseur/confirm_delete.html',context)
    elif request.method == 'POST':
        post.delete()
        messages.success(request,  'The post has been deleted successfully.')
        return redirect('/magasin/nouvFournisseur/')
# class TaskDetail (DetailView):
#     model = Fournisseur
#     context_object_name = 'fournisseur'
##hethom CRUD lil Produit
def edit_post(request, id):
    post = get_object_or_404(Produit, id=id)

    if request.method == 'GET':
        context = {'form': ProduitForm(instance=post), 'id': id}
        return render(request,'magasin/produit/editProduit.html',context)
    elif request.method == 'POST':
         form = ProduitForm(request.POST,  instance=post)
         if form.is_valid():
              form.save()
              messages.success(request, 'The post has been updated successfully.')
              return redirect('/magasin')
         else:
            messages.error(request, 'Please correct the following errors:')
            return render(request,'magasin/produit/editProduit.html',{'form':form})
                              #######################
def delete_post(request, id):
    post = get_object_or_404(Produit, pk=id)
    context = {'post': post}    
    
    if request.method == 'GET':
        return render(request, 'magasin/produit/confirm_delete.html',context)
    elif request.method == 'POST':
        post.delete()
        messages.success(request,  'The post has been deleted successfully.')
        return redirect('/magasin')
class TaskDetail(DetailView):
    model = Produit
    context_object_name = 'produit'
    ##############################################
@login_required
def index(request):
     if request.user.is_authenticated:
        request.session['username'] = request.user.username


     products= Produit.objects.all()
     context={'products':products}
     return render( request,'magasin/vitrine.html ',context )
#############Fournisseur##########################
def nouveauFournisseur(request) :
     fournisseur= Fournisseur.objects.all()
     context={'fournisseur':fournisseur}
     return render( request,'magasin/fournisseur.html ',context )
#pour l'affichage lowel 
def ADDFournisseur(request):
     if request.method == "POST" :
          form = FournisseurForm(request.POST,request.FILES)
          if form.is_valid():
               form.save()
               return HttpResponseRedirect('/magasin/nouvFournisseur/')
     else :
          form = FournisseurForm() #créer formulaire vide
     fournisseur=Fournisseur.objects.all()
     return render(request,'magasin/majFournisseur.html',{'fournisseur':fournisseur , 'form':form})
#################Produit############################""
def ADDProduit(request):
     if request.method == "POST":
          form = ProduitForm(request.POST, request.FILES)
          if form.is_valid():
               form.save()
               return HttpResponseRedirect('/magasin')
     else:
          form = ProduitForm()
     produits = Produit.objects.all()
     return render(request, 'magasin/majProduits.html', {'produits': produits, 'form': form})
     
########################sign up ############################
def register(request):
     if request.method == 'POST' :
          form = UserCreationForm(request.POST)
          if form.is_valid():
               form.save()
               username = form.cleaned_data.get('username')
               password = form.cleaned_data.get('password1')
               email = form.cleaned_data.get('Email address')
               user = authenticate(username=username, password=password)
               login(request,user)
               messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')
               return redirect('login')
     else :
          form = UserCreationForm()
     return render(request,'registration/register.html',{'form' : form})
############### commande ##################
def add_commande(request):
    # Create an empty form for adding a new commande
    form = CommandeForm()

    if request.method == 'POST':
        # Fill the form with the submitted data
        form = CommandeForm(request.POST)

        if form.is_valid():
            # Save the commande instance to the database
            commande = form.save()

            # Add the selected products to the commande instance
            for produit_id in request.POST.getlist('produits'):
                produit = Produit.objects.get(id=produit_id)
                commande.produits.add(produit)

            # Update the totalCde field based on the selected products' prices
            total = sum([produit.prix for produit in commande.produits.all()])
            commande.totalCde = total
            commande.save()

            # Redirect to the detail view of the newly created commande
            return redirect('detailcomm', commande.pk)

    context = {
        'form': form,
        'produits': Produit.objects.all(),
    }

    return render(request, 'magasin/commande/cart.html', context)

def commande_detail(request,id):
    commande = get_object_or_404(Commande, pk=id)
    context = {
        'commande': commande
    }
    return render(request, 'magasin/commande/commande_detail.html', context)

########## Profile#############
class MyProfile(LoginRequiredMixin, View):
    def get(self, request):
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        
        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }
        
        return render(request, 'magasin/Profile/profile.html', context)
    
    def post(self,request):
        user_form = UserUpdateForm(
            request.POST, 
            instance=request.user
        )
        profile_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            
            messages.success(request,'Your profile has been updated successfully')
            
            return redirect('profile')
        else:
            context = {
                'user_form': user_form,
                'profile_form': profile_form
            }
            messages.error(request,'Error updating you profile')
            
            return render(request, 'magasin/Profile/profile.html', context)