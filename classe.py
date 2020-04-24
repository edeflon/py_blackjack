import random

class PileCarte:

    def __init__(self, name):
        self.name = name
        self.cartes = []

    def new_card(self):
        card_value = random.randrange(1, 12)
        self.cartes.append(card_value)
    # 52 cartes
    # 26 rouges / 26 noires
    # 13 carreaux / 13 coeurs / 13 piques / 13 trefles
    # 4 x 2, 3, 4, 5, 6, 7, 8, 9, 10, V, D, R, A

class Carte:

    def __init__(self, couleur, symbole, nom, valeur):
        self.couleur = couleur
        self.symbole = symbole
        self.nom = nom
        self.valeur = valeur


class Banque:

    def __init__(self):
        self.pile_cartes = PileCarte("pile_banque")
        self.argent = 0
        self.score = 0


class Joueur:

    def __init__(self, argent: int):
        self.pile_cartes = PileCarte("pile_joueur")
        self.mise = 0
        self.score = 0
        self.argent = argent # VOIR POUR GERER LES ERREURS EN CAS DE STR
