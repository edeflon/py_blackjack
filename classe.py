import random


class PileCarte:

    def __init__(self, name):
        self.name = name
        self.cartes = []

    # CREATE
    def build(self):
        for nombre_de_deck in range(6):
            for symbole in ["Coeur", "Carreau", "Pique", "Trèfle"]:
                for value in range(1, 14):
                    self.cartes.append(Carte(symbole, value))

    # READ
    def __getitem__(self, item):
        return self.cartes[item]

    def show_pile(self):
        return f"{self.cartes}"

    def show_first_card(self):
        if self.cartes:
            return f"{self.cartes[0]}"
        else:
            return f"{self.cartes}"

    # UPDATE
    def add_card(self, card):
        return self.cartes.append(card)

    def remove_card(self, card_id):
        return self.cartes.pop(card_id)

    # DELETE
    def reset(self):
        self.cartes = []

    def shuffle(self):
        return random.shuffle(self.cartes)

    # AUTRES FONCTIONS
    def __len__(self):
        return len(self.cartes)

    def __str__(self):
        return f"{self.cartes}"


class Carte:

    def __init__(self, symbole, valeur):
        self.symbole = symbole

        if valeur == 1:
            self.valeur = 11
            self.name = "As"
        elif valeur == 11:
            self.valeur = 10
            self.name = "Valet"
        elif valeur == 12:
            self.valeur = 10
            self.name = "Dame"
        elif valeur == 13:
            self.valeur = 10
            self.name = "Roi"
        else:
            self.valeur = valeur
            self.name = str(valeur)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"{self.name} de {self.symbole}"


class Banque:

    def __init__(self):
        self.name = "banque"
        self.pile_cartes = PileCarte("pile_banque")
        self.argent = 0
        self.score = 0
        self.blackjack = False
        self.timetoplay = 0

    def calcul_score(self):
        score = 0

        for carte in self.pile_cartes:
            score += carte.valeur

        self.score = score


class Joueur:

    def __init__(self):
        self.name = "joueur"
        self.pile_cartes = PileCarte("pile_joueur")
        self.mise = 0
        self.score = 0
        self.blackjack = False
        self.timetoplay = 0
        self.argent = 0
        self.ace = False

    def miser(self, mise):
        self.mise += mise
        self.argent = self.argent - mise

    def calcul_score(self):
        score = 0

        for carte in self.pile_cartes:
            score += carte.valeur

        self.score = score
