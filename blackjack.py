import constante
import classe
import fonction

banque = classe.Banque()
jeu_de_cartes = classe.PileCarte("Jeu")

play = input("Voulez-vous jouer au Blackjack ? Q pour quitter. ")

# de 1 à 7 joueurs
joueur = classe.Joueur(fonction.int_input("Combien avez-vous pour vos mises ? (Minimum 5€) : "))  # pour l'instant on a un joueur

while play.lower() != "q":
    # on prépare le deck de 312 cartes
    jeu_de_cartes.build()
    jeu_de_cartes.shuffle()
    cartes_distribuees = 0

    # les joueurs misent (minimum 5€)
    joueur.miser("Combien voulez-vous parier ? (Minimum 5€) : ")
    print(joueur.mise, joueur.argent)

    # le croupier distribue les cartes
    fonction.distribuer_debut_partie(cartes_distribuees, jeu_de_cartes, banque, joueur)

    # on affiche les cartes (1 visible pour le croupier, 2 pour le joueur)
    print(f"BANQUE : {banque.pile_cartes.cartes[0]}")
    print(f"JOUEUR : {joueur.pile_cartes}")

    # on calcule le montant actuel des cartes
    montant_joueur = joueur.pile_cartes.calcul_montant()
    print(montant_joueur)

    # on vérifie si BlackJack ou non
    blackjack = joueur.pile_cartes.is_it_a_blackjack(montant_joueur)
    if blackjack:
        print("BLACKJACK ! Vous gagnez.")
        play = "q"

    # tour du joueur (carte ou rester)

    # tour du croupier

    # vérification du gagnant

    # répartition des gains

    # réinitialisation des jeux
    joueur.pile_cartes.reset()
    banque.pile_cartes.reset()

    if joueur.argent == 0:
        print("Vous n'avez plus d'argent. A bientôt")
        play = "q"
    else:
        play = input("Voulez-vous continuer à jouer au Blackjack ? Q pour quitter. ")
