from flask import *

import classe
import fonction

app = Flask(__name__)

banque = classe.Banque()
# Pour l'instant on n'a qu'un joueur
joueur = classe.Joueur()
jeu_de_cartes = classe.PileCarte("Jeu")

@app.route('/')
def home_page():
    return render_template('index_game.html')


@app.route('/play_game')
def play_game():
    mises = [5, 10, 20, 50, 100, 500]
    return render_template('play_game.html', joueur=joueur, banque=banque, deck=jeu_de_cartes, mises=mises)


@app.route('/start_game', methods=['POST'])
def start_game():
    jeu_de_cartes.build()
    jeu_de_cartes.shuffle()

    banque.pile_cartes.reset()
    banque.timetoplay = 0
    banque.score = 0

    joueur.pile_cartes.reset()
    joueur.timetoplay = 0
    joueur.argent = request.form.get('argent', type=int)
    joueur.mise = 0
    joueur.score = 0

    return redirect('/play_game')


@app.route('/miser/<int:mise>', methods=['GET'])
def miser(mise):
    if joueur.argent < mise:
        return redirect('/play_game')

    joueur.miser(mise)
    return redirect('/play_game')


@app.route('/lancer_manche')
def lancer_manche():
    joueur.timetoplay = 1
    fonction.distribuer_debut_partie(jeu_de_cartes, banque, joueur)
    calcul_score(joueur)
    calcul_score(banque)
    if joueur.score == 21:
        blackjack(joueur)
        tour_de_la_banque()
    return redirect('/play_game')


@app.route('/carte')
def carte():
    jouer(joueur)
    if joueur.score > 21:
        tour_de_la_banque()
    return redirect('/play_game')


@app.route('/rester')
def rester():
    return tour_de_la_banque()


def tour_de_la_banque():
    banque.timetoplay = 1
    blackjack(banque)

    if not banque.blackjack:
        while banque.score < 17:
            jouer(banque)

    return verification_gagnant()


def jouer(player):
    fonction.distribuer(jeu_de_cartes, player)
    fonction.remove_carte_distribuee(jeu_de_cartes)
    calcul_score(player)
    return redirect('/play_game')


def calcul_score(player):
    player.calcul_score()


def blackjack(player):
    player.blackjack = fonction.is_it_a_blackjack(player.score)


def verification_gagnant():
    result = fonction.winner(joueur.blackjack, banque.blackjack, joueur.score, banque.score)
    joueur.timetoplay = 2
    return repartition_gains(result)


def repartition_gains(resultat):
    if resultat == "T":  # TIE
        joueur.argent += joueur.mise
    elif resultat == "W":  # WIN
        joueur.argent += (joueur.mise*2)
    elif resultat == "WB":  # WIN par BLACKJACK
        joueur.argent += (joueur.mise*2.5)

    joueur.mise = 0

    return redirect('/play_game')


@app.route('/rejouer')
def fin_de_manche():
    joueur.pile_cartes.reset()
    joueur.timetoplay = 0
    joueur.mise = 0
    joueur.score = 0

    banque.pile_cartes.reset()
    banque.score = 0
    banque.timetoplay = 0

    if joueur.argent < 5:
        print("Vous n'avez plus assez d'argent pour participer. A bientôt")

    return redirect('/play_game')

if __name__ == "__main__":
    app.run(debug=True)