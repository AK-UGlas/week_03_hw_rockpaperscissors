from models.player import Player
from random import choice

class Game():
    """ a game class with functions to play the game ROCK PAPER SCISSORS """
    def __init__(self):
        self.player1 = None
        self.player2 = None

    def play_game(self, *args):
        # play a game of rock paper scissors
        # compare the weapon (gesture) of 2 players and decide the outcome based on the following rules:
        #   Rock beats Scissors
        #   Scissors beats Paper
        #   Paper beats Rock
        # If both weapons are equal, it's a draw

        # valididate input (should be a list of 1 or 2 Player objects)
        if len(args) == 0:
            return "not enough players added to the game"
        elif len(args) < 3:
            for player in args:
                if type(player) != Player:
                    return "Invalid input: Please enter valid player"
        else: 
            return "too many players: Only 2 players can be added to the game"

        self._assign_players(args)

        # if weapons are equal, it's a draw
        if self.player1.weapon == self.player2.weapon:
            return

        # check all possible winning scenarios for player1
        if self.player1.weapon == "rock" and self.player2.weapon == "scissors":
            return self.player1
        if self.player1.weapon == "paper" and self.player2.weapon == "rock":
            return self.player1
        if self.player1.weapon == "scissors" and self.player2.weapon == "paper":
            return self.player1 

        # if we make it this far, player2 must have won
        return self.player2 
        

    def _assign_players(self, players):
        # if no second player is present, create a computer player
        # and assign a random choice of weapon
        self.player1 = players[0]

        if len(players) == 2:
            self.player2 = players[1]
        else:
            weapons = ["rock", "paper", "scissors"]
            self.player2 = Player("computer", choice(weapons))
            