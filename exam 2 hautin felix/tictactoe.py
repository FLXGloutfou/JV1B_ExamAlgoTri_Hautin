plateau = ["1","2","3","4","5","6","7","8","9"]
fin = True
coup = 0
win =0

def afficher_plateau():
    for i in range (0,9,3):
        print (" | ".join(plateau[i:i+3]))
        if i < 6:
            print("-"*9)


def verifier (symbole) :
    lignes = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    return any(all(plateau[i] == symbole for i in groupe) for groupe in lignes)
    

joueur = "X"

while fin == True :
    afficher_plateau()
    coup = int(input(f"C'est au tour du joueur {joueur}. Entrez un nombre de 1 à 9 : ")) - 1

    if plateau[coup] == "1"or"2"or"3"or"4"or"5"or"6"or"7"or"8"or"9" :
        plateau[coup] = joueur
        if verifier (joueur):
            afficher_plateau()
            print(f"Le joueur {joueur} a gagné !")
            fin = False
        elif "1"and"2"and"3"and"4"and"5"and"6"and"7"and"8"and"9" not in plateau :
            afficher_plateau()
            print("Match nul !")
            fin = False
        joueur = "O" if joueur == "X" else "X"
    else:
        print("Case déjà occupée. Réessayez.")



#Pour faire un puissance 4 il faudra agrandir la taille de tableau original. Ensuite il faut uniquement demandé la colone dans laquel mettre son jeton.
#Puis mettre le jeton au plus bas possible de la colonne choissit. Puis faire une validation sur un alignement de 4 et non plus de toute la longeure du plateau de jeux.

