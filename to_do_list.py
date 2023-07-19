# Le programme doit permettre de réaliser 5 actions :

#     Ajouter un élément à la liste de courses

#     Retirer un élément de la liste de courses

#     Afficher les éléments de la liste de courses

#     Vider la liste de courses

#     Quitter le programme

# Tu dois donc demander à l'utilisateur de choisir parmi une de ces action en entrant un nombre de 1 à 5.

# Tu dois gérer le cas de figure où l'utilisateur ne rentre pas un nombre compris entre 1 et 5 ou s'il rentre par exemple des lettres ou un autre symbole invalide. Dans ce cas, tu dois afficher de nouveau le menu avec les options disponibles, jusqu'à ce que l'utilisateur choisisse une option valide.

choices = [
    "Ajouter un élément à la liste de courses", 
    "Retirer un élément de la liste de courses", 
    "Afficher les éléments de la liste de courses", 
    "Vider la liste de courses", 
    "Quitter le programme"
]
choice = 0
liste = []

while choice != "5" :
    print("Veuillez faire un choix dans la liste suivante: ")
    for i, element in enumerate(choices) :
        print(f"{i + 1}:", element)
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
        if len(liste) < 1 :
            print("🙈 Il n'y a aucun élément à afficher dans la liste.")
        else : 
            for i, element in enumerate(liste) :
                print(i + 1, element)  
    elif choice == "4" :
        if len(liste) > 1 :
            liste.clear()
        print("Tous les éléments de la liste ont été supprimés.")
    else :
        if choice == "5" :
            print("👋 À bientôt !")
        else :
            print("🙈 Choix incorrect")
    print("_________________________________________________")

