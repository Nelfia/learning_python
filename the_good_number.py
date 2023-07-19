import random

mystery_number = random.randint(0,100)
round_max = 5
turn = 0

print("✨ Le Jeu du Juste Nombre ✨")
while round_max != 0 :
    turn += 1
    print(f"Il te reste {round_max} essais")
    user_number = input("Devine le nombre : ")

    while not user_number.isdigit() or not (0 <= int(user_number) <= 100):
        print("Mauvaise entrée: tu dois donner un nombre compris entre 0 et 100 inclus.")
        user_number = input("Devine le nombre : ")

    user_number = int(user_number)
    if user_number == mystery_number :
        print(f"Bravo! Tu as réussi en {turn} essai(s). Le juste nombre est bien {mystery_number} !")
        break
    elif turn == 5 :
        print(f"Dommage, le juste nombre était {mystery_number}")
    elif mystery_number > user_number and turn != 5:
        print(f"Le juste nombre est plus GRAND que {user_number}")
    else :
        print(f"Le juste nombre est plus PETIT que {user_number}")

    round_max -= 1

