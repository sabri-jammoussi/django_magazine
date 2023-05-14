from django.db import models
from datetime import date
from django.contrib.auth.models import User

class Categorie (models.Model):
    TYPE_CHOICES=[
      ('Al','Alimentaire'),
      ('Mb','Meuble'),
      ('Sn','Sanitaire'),
      ('Vs','Vaisselle'),
      ('Vt','Vêtement'),
      ('Jx','Jouets'),
      ('Lg','Ligne de Maison'),
      ('Bj','Bijoux'),
      ('Dc','Décor')
    ]
    libelle=models.CharField( max_length=50,choices=TYPE_CHOICES,default='Al')
    def __str__(self):
      return 'Le nom = '+self.libelle
class Fournisseur(models.Model):
  nom=models.CharField( max_length=100)
  adresse=models.TextField(max_length=50,default='Tunis')
  email=models.EmailField( max_length=254)
  telephone=models.CharField( max_length=8)
  

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(
        default='avatar.jpg', # default avatar
        upload_to='profile_avatars' # dir to store the image
    )

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        # save the profile first
        super().save(*args, **kwargs)

        # resize the image
        img = Image.open(self.avatar.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            # create a thumbnail
            img.thumbnail(output_size)
            # overwrite the larger image
            img.save(self.avatar.path)
class Produit(models.Model):
    TYPE_CHOICES=[
      ('em','emballé'),
      ('fr','Frais'),
      ('cs','Conserve')
      ]
    libellé = models.CharField(max_length=100,default='a ')
    description = models.TextField(default='non definie')
    prix = models.DecimalField(max_digits=10,decimal_places=3,default=0)
    type = models.CharField(max_length=2,choices=TYPE_CHOICES,default='em')
    image=models.ImageField(blank=True,upload_to='media/')
    categorie=models.ForeignKey(Categorie,on_delete=models.CASCADE,null=True)
    fournisseur=models.ForeignKey(Fournisseur,on_delete=models.CASCADE,null=True)
    
    def __str__(self):
      return 'la libelle= '+self.libellé+' la description= '+self.description+' le prix = '+str(self.prix)+' le type='+self.type
class ProduitNC(Produit):
    Duree_garantie=models.CharField(max_length=100)

    def __str__(self):
        return "libelle : "+self.libelle+" Prix : "+str(self.prix)+ "Garantie : "+self.Duree_garantie
class Commande (models.Model):
    dateCde = models.DateField(null=True, default=date.today)
    totalCde = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    produits = models.ManyToManyField('Produit')
    fournisseurs = models.ManyToManyField('Fournisseur')

    def __str__(self):
        return f"({self.dateCde},{self.totalCde} )"
# Create your models here.

        # return self.libellé+","+self.description+"," + str(self.prix)+"," + self.type