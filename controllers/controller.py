from flask import render_template, request
from app import app
from models.game import Game
from models.player import Player

# declare instance of Game class here. we can reuse any time a new game starts
rps = Game()

@app.route("/")
def home():
    return render_template("index.html", title='Welcome')

@app.route("/", methods=["POST"])
def play_game():
    winner = None
    player1 = Player(request.form["name-1"], request.form["weapon-1"])

    # check both player details have been completed
    if request.form.get('name-2'):
        player2 = Player(request.form["name-2"], request.form["weapon-2"])
        winner = rps.play_game(player1, player2)
    else:
        winner = rps.play_game(player1)

    return render_template('result.html', title='Result', winner=winner, weapon=winner.weapon if winner else player1.weapon)