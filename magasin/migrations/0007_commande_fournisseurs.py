# Generated by Django 4.2.1 on 2023-05-13 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0006_alter_commande_totalcde'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='fournisseurs',
            field=models.ManyToManyField(to='magasin.fournisseur'),
        ),
    ]
