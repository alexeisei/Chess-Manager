from controllers import PlayerController
from controllers import TournamentController
from gamecontroller import GameController

if __name__ == "__main__":
    players = PlayerController()
    tournament = TournamentController()
    start = GameController(players, tournament)
