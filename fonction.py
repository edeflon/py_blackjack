def distribuer_debut_partie(jeu, banque, *joueurs):
    list_joueur = [joueur for joueur in joueurs]

    while len(banque.pile_cartes) < 2:
        for joueur in list_joueur:
            distribuer(jeu, joueur)
            remove_carte_distribuee(jeu)
            distribuer(jeu, banque)
            remove_carte_distribuee(jeu)


def distribuer(jeu, player):
    carte = is_it_an_ace(jeu, player)
    player.pile_cartes.add_card(carte)


def is_it_an_ace(jeu, player):
    if jeu[0].valeur == 11 and player.name != "banque":
        return valeur_ace_joueur(jeu[0], player)
    elif jeu[0].valeur == 11 and player.name == "banque":
        return valeur_ace_banque(jeu[0], player)
    else:
        return jeu[0]


def valeur_ace_joueur(carte, joueur):
    if not joueur.blackjack:
        joueur.ace = True

    return carte


def valeur_ace_banque(carte, banque):
    if banque.blackjack:
        return carte
    else:
        banque.calcul_score()
        banque.score += carte.valeur
        if banque.score > 21:
            carte.valeur = 1
            return carte

    return carte


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

