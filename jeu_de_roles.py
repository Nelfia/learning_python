import random

pv_user = 50
user_potions = 3
pv_ennemy = 50

while (pv_user > 0 and pv_ennemy > 0):
    user_choice = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")

    while user_choice != "1" and user_choice != "2":
        user_choice = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")

    if user_choice == "1":
        # Attaque utilisateur :
        user_damage = random.randint(5,10)
        print(f"⚔️\tVous avez infligé {user_damage} points de dégats à l'ennemi.")
        pv_ennemy -= user_damage

        if pv_ennemy <= 0 :
            print("🥳\tVous avez gagné 💪")
            break

        # Attaque de l'ennemi:
        ennemy_damage = random.randint(5,15)
        print(f"⚔️\tL'ennemi vous a infligé {ennemy_damage} points de dégats.")
        pv_user -= ennemy_damage
        # Bilan de l'attaque :
        print(f"❤️\tIl vous reste {pv_user} points de vie.")
        print(f"❤️\tIl reste {pv_ennemy} points de vie à l'ennemi.")

    elif user_choice == "2":
        if user_potions == 0 :
            print("Vous n'avez plus de potion disponible!")
            continue
        else :
            # Utilisation potion:
            potion = random.randint(15, 50)
            print(potion)
            pv_user += potion
            user_potions -= 1
            print(f"🪄\tVous récupérez {potion} points de vie ❤️. (🍺 {user_potions} restantes)")

            # Attaque de l'ennemi:
            ennemy_damage = random.randint(5,15)
            pv_user -= ennemy_damage
            print(f"⚔️\tL'ennemi vous a infligé {ennemy_damage} points de dégats.")

            # Bilan de l'attaque :
            print(f"❤️\tIl vous reste {pv_user} points de vie.")
            print(f"❤️\tIl reste {pv_ennemy} points de vie à l'ennemi.")

            # Tour passé :
            print("____________________________________________________________")
            print("Vous passez votre tour...")
            
            # Attaque de l'ennemi:
            ennemy_damage = random.randint(5,15)
            pv_user -= ennemy_damage
            print(f"⚔️\tL'ennemi vous a infligé {ennemy_damage} points de dégats.")

            # Bilan de l'attaque :
            print(f"❤️\tIl vous reste {pv_user} points de vie.")
            print(f"❤️\tIl reste {pv_ennemy} points de vie à l'ennemi.")

    if pv_user <= 0 :
        print("😒\tVous avez perdu 😵‍💫")
        break
    print("____________________________________________________________")

print('Fin du jeu.')
