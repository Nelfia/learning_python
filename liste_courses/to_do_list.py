import os
import json

choices = [
    "Ajouter un élément à la liste de courses", 
    "Retirer un élément de la liste de courses", 
    "Afficher les éléments de la liste de courses", 
    "Vider la liste de courses", 
    "Quitter le programme"
]
choice = 0

# Fichier de sauvegarde liste de courses
# chemin = r"D:\desktop\python\formation\pratique\liste_courses\liste.json"
CUR_DIR = os.path.dirname(__file__)
chemin = os.path.join(CUR_DIR, "liste.json")

# Vérification présence fichier:
if os.path.exists(chemin) :
    with open(chemin, "r", encoding="utf-8") as file :
        liste = json.load(file)
        print(liste)
else :
    liste = []

while choice != "5" :
    print("Veuillez faire un choix dans la liste suivante: ")
    for i, element in enumerate(choices, 1) :
        print(f"{i}:", element)
    choice = input("👉 Votre choix: ")
    
    elt = ""
    
    if choice == "1" :
        while len(elt) == 0 :
            elt = input("Entrez le nom d'un élément à ajouter à la liste: ")
        liste.append(elt)
        print(f"✔️ L'élément {elt} a bien été ajouté à la liste.")
    elif choice == "2" :
        if len(liste) < 1 :
            print("🙈 Il n'y a aucun élément dans la liste.")
        else :
            while len(elt) == 0 :
                elt = input("Entrez le nom d'un élément à supprimer de la liste: ")
            if elt in liste :
                liste.remove(elt)
                print(f"✔️ L'élément {elt} a bien été supprimé de la liste.")
            else :
                print(f"🙈 Aucun élément {elt} dans la liste.")
    elif choice == "3" :
        if not liste:
            liste = []
        if len(liste) < 1 :
            print("🙈 Il n'y a aucun élément à afficher dans la liste.")
        else : 
            for i, element in enumerate(liste, 1) :
                print(i, element)  
    elif choice == "4" :
        if len(liste) > 1 :
            liste = liste.clear()
            liste = []
        print("Tous les éléments de la liste ont été supprimés.")
    elif choice == "5" :
        print("👋 À bientôt !")
    else :
        print("🙈 Choix incorrect")
    print("_________________________________________________")

with open(chemin, "w") as file: 
    json.dump(liste, file, indent=4)

