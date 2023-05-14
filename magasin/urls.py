from django.urls import URLPattern, path, include
from . import views
from .views import TaskDetail,MyProfile
from django.contrib.auth.views import ( 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
urlpatterns = [
        path('',views.index, name='index'),
        ####path of CRUD for Produit ##############
        path('Produit/edit/<int:id>/', views.edit_post, name='editProduit'),
        path('Produit/delete/<int:id>/', views.delete_post, name='deleteProduit'),
        path('Produit/detail/<int:pk>/',TaskDetail.as_view(),name='detail'),
        ####path of CRUD for Fournisseur##############
        path('Fournisseur/edit/<int:id>/', views.edit_fournisseur, name='editFournisseur'),
        path('Fournisseur/delete/<int:id>/', views.delete_fournisseur, name='deleteFournisseur'),
        # path('Fournisseur/detail/<int:pk>/',TaskDetail.as_view(),name='fournisseurdetail'),
        ##################################################
        path('register/',views.register, name = 'register'), 
        path('ADDProduit/',views.ADDProduit,name='ADDProduit'),
        path('nouvFournisseur/',views.nouveauFournisseur,name='nouveauFour'),
        path('ADDFournisseur/',views.ADDFournisseur,name='ADDFournisseur'),
         ##########Reset Password ##########################
        path('password-reset/', PasswordResetView.as_view(template_name='magasin/password_reset.html',html_email_template_name='magasin/password_reset_email.html'),name='password-reset'),
        path('password-reset/done/', PasswordResetDoneView.as_view(template_name='magasin/password_reset_done.html'),name='password_reset_done'),
        path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='magasin/password_reset_confirm.html'),name='password_reset_confirm'),
        path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='magasin/password_reset_complete.html'),name='password_reset_complete'),
        ########### add Commande ###################
        path("add_commande",views.add_commande,name="Commande"),
        path('detail_commande/<int:id>/',views.commande_detail,name="detailcomm"),
        path('profile/', MyProfile.as_view(), name='profile'),
         
]
