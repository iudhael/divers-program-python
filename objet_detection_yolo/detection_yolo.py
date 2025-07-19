from ultralytics import YOLO

model = YOLO("yolo11n.pt")
#verbose empeche l'affichage des logs
#show affiche une fenetre  avec la video et les rectangle sur chaque ojet avec leur classe
#save permet d'enregisrer le resultat
new_img = model(source="/home/iudhael/Téléchargements/test_video.mp4", save=False, show=True, verbose=False )

"""
for resultat in new_img:
    boxes = resultat.boxes
    classe_names = resultat.names
    #print(classe_names)
    for boxe in boxes:
        class_id = int(boxe.cls[0]) # box.cls est un tenseur, d'où [0] pour la première (et unique) valeur

        # Utiliser l'ID pour trouver le nom de la classe
        object_name = classe_names[class_id]
        print(object_name)

"""

