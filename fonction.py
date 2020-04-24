


while len(banque) < 2:
    joueur.append(jeu_de_cartes[cartes_distribuees])
    cartes_distribuees += 1
    banque.append(jeu_de_cartes[cartes_distribuees])
    cartes_distribuees += 1

for carte, valeur in joueur:
    cartes_joueur[carte] = valeur
    montant_joueur = sum(cartes_joueur.values())

for carte, valeur in banque:
    cartes_banque[carte] = valeur
    montant_banque = sum(cartes_banque.values())

if montant_joueur == 21:
    print("BLACKJACK ! Vous avez gagné.")
    sys.exit()

choice = input("Une autre carte ? R pour s'arrêter ")

while choice.lower() != "r":
    joueur.append(jeu_de_cartes[cartes_distribuees])
    cartes_distribuees += 1

    for carte, valeur in joueur:
        cartes_joueur[carte] = valeur
        montant_joueur = sum(cartes_joueur.values())

    if montant_joueur > 21:
        print(f"BANQUE : {cartes_banque}, {montant_banque}")
        print(f"JOUEUR : {cartes_joueur}, {montant_joueur}")
        print("Vous avez perdu !")
        sys.exit()

    print(f"BANQUE : {cartes_banque}")
    print(f"JOUEUR : {cartes_joueur}, {montant_joueur}")

    choice = input("Une autre carte ? C pour Carte, R pour Rester")

print(f"BANQUE : {cartes_banque}, {montant_banque}")
print(f"JOUEUR : {cartes_joueur}, {montant_joueur}")

while montant_banque < 17:
    banque.append(jeu_de_cartes[cartes_distribuees])
    cartes_distribuees += 1

    for carte, valeur in banque:
        cartes_banque[carte] = valeur
        montant_banque = sum(cartes_banque.values())

    print(f"BANQUE : {cartes_banque}, {montant_banque}")
    print(f"JOUEUR : {cartes_joueur}, {montant_joueur}")

if montant_joueur > 21:
    print("Vous avez perdu !")
elif montant_joueur > montant_banque:
    print("Vous avez gagné !")
elif montant_banque > 21:
    print("Vous avez gagné !")
elif montant_banque > montant_joueur:
    print("Vous avez perdu !")



# la banque va distribuer les cartes : 1 visible par joueur et 1 pour lui
# la banque va distribuer une seconde carte visible par joueur et 1 cachée pour lui

# la banque tire à 16, reste à 17
