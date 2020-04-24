import random
import sys

import constante
import classe

play = input("Voulez-vous jouer au Blackjack ? Q pour quitter. ")

while play.lower() != "q":
    jeu_de_cartes = random.sample(constante.CARTES, len(constante.CARTES))
    cartes_distribuees = 0

    print(len(constante.CARTES))

    banque = classe.Banque()
    joueur = classe.Joueur(int(input("Entrez la somme d'argent que vous avez amené : ")))

    joueur.pile_cartes.new_card()
    print(joueur.pile_cartes)

    play = input("Voulez-vous continuer à jouer au Blackjack ? Q pour quitter. ")

print(joueur.argent)
