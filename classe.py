import random

import fonction

class PileCarte:

    def __init__(self, name):
        self.name = name
        self.cartes = []

    def build(self):
        for nombre_de_deck in range(6):
            for symbole in ["Coeur", "Carreau", "Pique", "Trèfle"]:
                for value in range(1, 14):
                    self.cartes.append(Carte(symbole, value))

    def add_card(self, card):
        return self.cartes.append(card)

    def shuffle(self):
        return random.shuffle(self.cartes)

    def calcul_montant(self):
        montant = 0

        for carte in self.cartes:
            montant += carte.valeur

        return montant

    def is_it_a_blackjack(self, montant):
        if montant == 21:
            return True

        return False

    def reset(self):
        self.cartes = []

    def __getitem__(self, item):
        return self.cartes[item]

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
            self.name = valeur

    def as_value(self):
        value = input("Souhaitez-vous que la valeur de votre As soit 1 ou 11 ?")

        while value != "1" or value != "11":
            value = input("Veuillez entrer 1 ou 11.")

        return int(value)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"{self.name} de {self.symbole}"


class Banque:

    def __init__(self):
        self.pile_cartes = PileCarte("pile_banque")
        self.argent = 0
        self.score = 0


class Joueur:

    def __init__(self, argent):
        self.pile_cartes = PileCarte("pile_joueur")
        self.mise = 0
        self.score = 0

        while argent < 5:
            argent = fonction.int_input("Veuillez entrer un montant supérieur à 5€ : ")

        self.argent = argent # VOIR POUR GERER LES ERREURS EN CAS DE STR + INPUT DE L'ARGENT DU JOUEUR

    def miser(self, message):

        mise = fonction.int_input(message)

        while mise < 5:
            mise = fonction.int_input("Votre mise doit être supérieure ou égale à 5€ : ")

        self.mise = mise
        self.argent = self.argent - self.mise

