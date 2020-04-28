import random

import fonction

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
        return f"{self.cartes[0]}"

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
    def calcul_montant(self):
        montant = 0

        for carte in self.cartes:
            montant += carte.valeur

        return montant

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

        self.argent = argent

    def miser(self, message):

        mise = fonction.int_input(message)

        while mise < 5 or mise > self.argent:
            mise = fonction.int_input(f"Il vous reste {self.argent}€. Votre mise doit être comprise entre 5 et {self.argent}€ : ")

        self.mise = mise
        self.argent = self.argent - self.mise

