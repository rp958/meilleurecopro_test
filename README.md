# Test technique MeilleurCopro, Exercice 1

Voici un repo contenant l'exercice 1.

Il a été codé en Django. Un fichier requirements est inclus.

Formulaire pour ajouter une annonce du site bienici.com :
> api/fetch_and_insert/

Formulaire pour calculer les quantiles et moyennes :
>api/quantiles

Une commande a été ajoutée pour insérer les données à partir du fichier .csv :
> python manage.py import_dataset --path dataset_annonces.csv

Les lignes pour lesquelles une erreur est détectée ne sont pas insérées. Par exemple, on a ce type de message :
> Field 'zip_code' expected a number but got 'malakoff'.

Mes résultats sur l'intégralité des annoces insérées (celles pour lesquelles les charges ne sont pas renseignées ont été
exclues) sont les suivants:
> Nombre d'annonces sélectionnées: 925944
> 
> Charges moyennes : 12113.69
> 
> Quantile 10% : 360.0
> 
> Quantile 90% : 2940.0