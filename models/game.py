from models.player import Player

class Game():
    """ a game class with functions to play the game ROCK PAPER SCISSORS """
    def __init__(self):
        self.player1 = None
        self.player2 = None

    def play_rpc(self, *args):
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


    def _assign_players(self, players):
        # if no second player is present, create a computer player
        # and assign a random choice of weapon
        self.player1 = players[0]

        if len(args) == 1:
            weapon = ["rock", "paper", "scissors"]
            