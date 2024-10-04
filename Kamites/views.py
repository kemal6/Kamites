import os
from django.shortcuts import render
from django.shortcuts import render
from objectd.forms import ImageForm
import objectd.models

from PIL import Image
from ultralytics import YOLO
import requests
import numpy as np
import tensorflow as tf
import dill
import json

img =['im1','im2','im3']
objs=[
    {'id':1,'title':'first image','body':'sdfjodfj podjflsd'},
    {'id':2,'title':'fsecode image','body':'sdfjodfj podjflsd'},
    {'id':3,'title':'first image','body':'sdfjodfj podjflsd'},
    ]

def home(request):
    return render(request,'home.html',{'objs':objs})

def about(request):
    return render(request,'pages/about.html')

def contacts(request):
    return render(request,'pages/contacts.html')





##***********Modele*******************************
# Charger le modèle YOLOv8 personnalisé
model = YOLO("Kamites/best.pt")


# Définir une fonction qui prend en entrée une image et renvoie les résultats de la détection d'objets
def detect_objects(image):
    # Convertir l'image en tableau numpy
    #image = np.array(image)
    # Appeler la méthode detect du modèle YOLOv8
    #results = model.predict(image)
   
    
    # # Renvoyer le JSON

    result = model.predict(image)
    # classes = preds.boxes.cls
    # results = [model.names[int(cls)] for cls in classes]

    #Extraire les classes, les scores et les boîtes englobantes des objets détectés
    classes = result[0].boxes.cls
    scores = result[0].boxes.conf
    boxes = result[0].boxes.xyxy


    #Créer un dictionnaire JSON avec les résultats
    output = {"classes": classes, "scores": scores, "boxes": boxes}

    l=[]
    #, "scores": {scores[i]}, "boxes": {boxes[i]}
    # Afficher les résultats
    for i in range(len(classes.tolist())):
        l.append({"classe":result[0].names[classes.tolist()[i]] , "scores": scores.tolist()[i] , "boxes": "//".join([str(x) for x in boxes.tolist()[i]]) })
        


    res=json.dumps(l)
    return l


##*********Fin Modele*****************************










def image_view(request):
    if os.path.exists("Kamites/media/image.jpg"):
        os.remove("Kamites/media/image.jpg")
    f=False
    if request.method == "POST":
        #l=[]

        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image_file = form.cleaned_data["image"]
            image = Image.open(image_file)
            #im = im.convert("RGB")
            if image.format in ["JPG","JPEG"] :
                image.save("Kamites/media/image.jpg", format="JPEG", quality=100)
                detected=detect_objects("Kamites/media/image.jpg")
            else:
                return render(request, "home.html", {"form": form,"prem":False,"detected":[],"founded":f})

            l=[]
            
            
            
            if detected != []:
                f=True
                
                for obj in detected:
                    scr=obj["scores"]>0.24

                    if scr:
                        print("reconnu: "+ obj["classe"])
                        objd=objectd.models.Object.objects.filter(Nom__icontains=""+obj["classe"])[0]
                        r =objd
                            # "Nom":objd.Nom,
                            # "Description":objd.Description,
                            # "Ethnie":objd.Ethnie,
                            # "Pays":objd.Pays,
                            # "Materiaux":objd.Materiaux,
                            # "Hauteur_cm":objd.Hauteur_cm,
                            # "Largeur_cm":objd.Largeur_cm,
                            # "Poids":objd.Poids,
                            # "Datation":objd.Datation,
                            #"Zone":obj["boxes"]}
                        
                        
                        l.append(r)
                    else:
                        print("pas bien reconnu: "+ obj["classe"])
                    

        # Faites quelque chose avec l'image
        
        return render(request, "home.html", {"form": form,"prem":False,"detected":l,"founded":f})
    else:
        form = ImageForm()
    return render(request, "home.html", {"form": form,"prem":True,"detected":[],"founded":f})