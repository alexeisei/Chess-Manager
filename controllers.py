from models import Player
from models import Tournament
from views import Menu
from tinydb import TinyDB, Query


class PlayerController:
    """
    This class controls the player's related models and views
    """

    def __init__(self):
        """ constructor controller player"""
        self.player_view = Menu()
        self.playerdb = TinyDB("players.json")
        self.playerquery = Query()
        self.player_table = self.playerdb.table("players")

    def player_menu(self):
        """ start the player menu"""
        self.player_view.menu_player()
        input_choice = input()
        input_check_list = ["1", "2", "3", "4"]
        while input_choice not in input_check_list:
            input_choice = input()
        menu = input_check_list.index(input_choice)
        menu_list = [
            self.new_player,
            self.edit_player,
            self.players_list_tt,
        ]
        if menu == 3:
            pass
        else:
            menu_list[menu]()

    def new_player(self):

        """ Create a new player"""
        self.player_view.new_player_name()
        name = input()
        firstname = self.player_view.new_player_first_name()
        birth_date = self.player_view.new_player_birthdate()
        gender = self.player_view.new_player_gender()
        rank = self.player_view.new_player_rank()
        new_player = Player(name, firstname, birth_date, gender, rank)
        self.player_table.insert(new_player.serialized_player())
        self.player_menu()

    def edit_player(self):
        """  edit player Rank"""
        self.player_view.new_player_name()
        input_player = input()
        self.player_view.change_player_rank()
        try:
            input_rank = int(input())
        except ValueError:
            self.player_view.error_player_rank()
        else:
            self.player_table.update(
                {"Elo": input_rank}, self.playerquery.Last_name == f"{input_player}"
            )
        finally:
            self.player_menu()

    def players_list_tt(self):
        """ Create a list of all players"""
        players = self.player_table.all()
        for player in players:
            self.player_view.player_list(player)
        self.player_menu()

    def player_alpha_order(self):
        """ List of the player in alphabetical order"""
        players = self.player_table.all()
        alpha_order = sorted(players, key=lambda x: x["Last_name"])
        return alpha_order

    def player_ranking_order(self):
        """ List of the player in ranking order"""
        players = self.player_table.all()
        rank_order = sorted(players, key=lambda x: x["Rank"], reverse=True)
        return rank_order

    def search_player(self):
        """ search player"""
        self.player_view.new_player_name()
        input_player = input()
        player = self.player_table.search(
            self.playerquery.Last_name == f"{input_player}"
        )
        if len(player) == 1:
            return player[0]
        else:
            self.playerviews.error_add_player_lname()


class TournamentController:
    """
    This class controls the tournament's models and views
    """

    def __init__(self):
        """ constructor of the tournament controller"""
        self.tournament_view = Menu()
        self.tournamentdb = TinyDB("tournament.json")
        self.tournamentquery = Query()
        self.tournament_table = self.tournamentdb.table("tournament")

    def tournament_menu(self):
        """ start the tournament menu"""
        self.tournament_view.menu_tournament()
        input_choice = input()
        input_check_list = ["1", "2", "3"]
        while input_choice not in input_check_list:
            input_choice = input()
        index_menu = input_check_list.index(input_choice)
        menu_list = [
            self.new_tt,
            self.tt_list,
        ]
        if index_menu == 2:
            pass
        else:
            menu_list[index_menu]()

    def new_tt(self):
        """ create new tournament object """
        self.tournament_view.new_tournament_name()
        name = input()
        location = self.tournament_view.new_tournament_location()
        date = self.tournament_view.new_tournament_date()
        rounds_number = 4
        tt_list = ()
        pl_list = []
        timer = self.tournament_view.new_tournament_timer()
        description = self.tournament_view.new_tournament_description()
        new_tournament = Tournament(
            name, location, date, rounds_number, tt_list, pl_list, timer, description
        )
        self.tournament_table.insert(new_tournament.serialize_tournament())
        self.tournament_menu()

    def tt_list(self):
        """ create the list of all tournament """
        tournaments = self.tournament_table.all()
        for tournament in tournaments:
            self.tournament_view.tournament_list(tournament)
        self.tournament_menu()
