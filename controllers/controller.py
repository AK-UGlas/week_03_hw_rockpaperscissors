from flask import render_template, request
from app import app
from models.game import game
from models.player import player

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def play_game():
    print(request.form)