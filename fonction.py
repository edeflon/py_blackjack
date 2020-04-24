def int_input(message): # on vérifie que le contenu donné est bien un int
    number = input(message)

    while not number.isdigit():
        number = input("Merci d'entrer un nombre valide : ")

    return int(number)


def distribuer_debut_partie(counter: int, jeu, banque, *joueurs):
    list_joueur = [joueur for joueur in joueurs]

    while len(banque.pile_cartes) < 2:
        for joueur in list_joueur:
            joueur.pile_cartes.add_card(jeu[counter])
            counter += 1 # PB A REGLER
            banque.pile_cartes.add_card(jeu[counter])
            counter += 1
