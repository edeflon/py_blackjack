import constante
import classe
import fonction

banque = classe.Banque()
jeu_de_cartes = classe.PileCarte("Jeu")

play = input("Voulez-vous jouer au Blackjack ? Q pour quitter.\n")

# de 1 à 7 joueurs
joueur = classe.Joueur(fonction.int_input("Combien avez-vous pour vos mises ? (Minimum 5€) : "))  # pour l'instant on a un joueur

# on prépare le deck de 312 cartes
jeu_de_cartes.build()
jeu_de_cartes.shuffle()

while play.lower() != "q":
    # les joueurs misent (minimum 5€)
    joueur.miser("Combien voulez-vous parier ? (Minimum 5€) : ")
    print(f"Vous misez {joueur.mise} € ce tour.\n")

    # le croupier distribue les cartes
    fonction.distribuer_debut_partie(jeu_de_cartes, banque, joueur)

    # on affiche les cartes (1 visible pour le croupier, 2 pour le joueur)
    print(f"BANQUE : {banque.pile_cartes.show_first_card()}")
    print(f"JOUEUR : {joueur.pile_cartes.show_pile()}")

    # on calcule le montant actuel des cartes
    montant_joueur = joueur.pile_cartes.calcul_montant()
    blackjack_joueur = fonction.is_it_a_blackjack(montant_joueur)
    print(montant_joueur, blackjack_joueur, "\n")

    # tour du joueur (carte ou rester)
    continuer = input("Voulez-vous une nouvelle carte ou arrêter ? R pour arrêter :\n")

    while continuer.lower() != "r" or montant_joueur < 17:
        fonction.distribuer(jeu_de_cartes, joueur)
        fonction.remove_carte_distribuee(jeu_de_cartes)
        montant_joueur = joueur.pile_cartes.calcul_montant()
        print(joueur.pile_cartes.show_pile(), montant_joueur)

        if montant_joueur > 21:
            continuer = "r"
        else:
            continuer = input("Voulez-vous une nouvelle carte ou arrêter ? R pour arrêter :\n")

    # tour du croupier
    print(f"BANQUE : {banque.pile_cartes.show_pile()}")
    print(f"JOUEUR : {joueur.pile_cartes.show_pile()}")
    montant_banque = banque.pile_cartes.calcul_montant()
    blackjack_banque = fonction.is_it_a_blackjack(montant_banque)
    print(montant_banque, blackjack_banque, "\n")

    while montant_banque < 17:
        fonction.distribuer(jeu_de_cartes, banque)
        fonction.remove_carte_distribuee(jeu_de_cartes)
        montant_banque = banque.pile_cartes.calcul_montant()
        print(f"BANQUE : {banque.pile_cartes.show_pile()}, score de {montant_banque}")

    # vérification du gagnant
    result = fonction.winner(blackjack_joueur, blackjack_banque, montant_joueur, montant_banque)

    # répartition des gains
    if result == "T":  # TIE
        joueur.argent += joueur.mise
    elif result == "W":  # WIN
        joueur.argent += (joueur.mise*2)
    elif result == "WB":  # WIN par BLACKJACK
        joueur.argent += (joueur.mise*2.5)

    print(f"Vous avez désormais {joueur.argent}.\n")

    # réinitialisation des jeux
    joueur.pile_cartes.reset()
    banque.pile_cartes.reset()

    if joueur.argent < 5:
        print("Vous n'avez plus assez d'argent pour participer. A bientôt")
        play = "q"
    else:
        play = input("Voulez-vous continuer à jouer au Blackjack ? Q pour quitter. ")
