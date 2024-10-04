from django.shortcuts import render
from .forms import ImageForm
from .mocks import Objectd
from .models import Object
import csv
import os


# Create your views here.
# def chargement(request):
#     # print( os.path.exists('objectd/Data_Objects.csv'))
#     with open('objectd/Data_Objects.csv', 'r') as f:
#         print('fichierr ouvert')
#         reader = csv.reader(f)
#         next(reader) # Pour ignorer la ligne d'en-tête

#         for row in reader:
#                 Nom,Description,Ethnie,Pays,Materiaux,Hauteur_cm,Largeur_cm,Poids,Datation,img,img1,img2,img3,img4,img5,img6,img7,img8,img9,img10,img11,img12 = row
#                 object = Object(Nom=Nom ,Description=Description  ,Ethnie=Ethnie  ,Pays=Pays ,Materiaux= Materiaux ,Hauteur_cm=Hauteur_cm  ,Largeur_cm=Largeur_cm  ,Poids=Poids  ,Datation=Datation ,img=img  ,img1= img1 ,img2=img2  ,img3=img3  ,img4=img4  ,img5=img5  ,img6=img6  ,img7=img7  ,img8=img8  ,img9=img9  ,img10=img10  ,img11=img11  ,img12=img12)
#                 object.save()
#     return pass

def index(request):
    objs=Object.objects.all()
    return render(request,'objectd/index.html',{'objs':objs})

def show(request,id):
    try:
        objs=Object.objects.get(id=id)
        return render(request,'objectd/show.html',{'obj':objs})
    except:
        return render(request,'objectd/404.html') 
    

