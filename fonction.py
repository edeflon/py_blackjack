import classe

def int_input(message): # on vérifie que le contenu donné est bien un int
    number = input(message)

    while not number.isdigit():
        number = input("Merci d'entrer un nombre valide : ")

    return int(number)


def distribuer_debut_partie(jeu, banque, *joueurs):
    list_joueur = [joueur for joueur in joueurs]

    while len(banque.pile_cartes) < 2:
        for joueur in list_joueur:
            distribuer(jeu, joueur)
            remove_carte_distribuee(jeu)
            distribuer(jeu, banque)
            remove_carte_distribuee(jeu)


def distribuer(jeu, joueur):
    joueur.pile_cartes.add_card(jeu[0])


def remove_carte_distribuee(jeu):
    jeu.remove_card(0)


def is_it_a_blackjack(score):
    if score == 21:
        return True

    return False


def winner(blackjack_joueur, blackjack_banque, montant_joueur, montant_banque):
    if blackjack_joueur or blackjack_banque:
        return blackjack_result(blackjack_joueur, blackjack_banque, montant_banque)

    if montant_joueur > 21:
        return "L"
    elif montant_banque > 21:
        return "W"
    elif montant_joueur == montant_banque:
        return "T"
    elif montant_banque > montant_joueur:
        return "L"
    elif montant_joueur > montant_banque:
        return "W"


def blackjack_result(blackjack_joueur, blackjack_banque, montant_banque):
    if blackjack_joueur and not blackjack_banque and montant_banque == 21:
        return "WB"
    elif blackjack_joueur and blackjack_banque:
        return "T"
    elif blackjack_banque and not blackjack_joueur:
        return "L"
    elif blackjack_joueur:
        return "WB"

