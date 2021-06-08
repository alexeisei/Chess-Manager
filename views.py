

class Menu:
    """
    This class sets the "views" of the chess application, the user will interact with
    """

    # Main menu
    def main_menu(self):
        """ print the Main menu """
        print("--------- Main Menu ---------")
        print("Welcome, please select your action and press Enter")
        print("1.Manage Tournament")
        print("2.Manage Player")
        print("3.Start Tournament")
        print("4.Report")
        print("Q.Quit the application")
        print("Choose your action please")
        print("------------------------------")

    # Player menu
    def menu_player(self):
        """ print the Player menu """
        print("--------- Player Menu ---------")
        print("Please select your action and press Enter")
        print("1.New player")
        print("2.Edit player's rank")
        print("3.Players' list")
        print("4.Return to Main menu")
        print("-------------------------------")

    def new_player_name(self):
        """ get the player last name """
        print("Type in player's Last Name: ")
        name = input()
        return name

    def new_player_first_name(self):
        """ get the player firt name """
        print("Type in player's First Name: ")
        first_name = input()
        return first_name

    def new_player_birthdate(self):
        """ get the player Birth date """
        print("Type in player's Birth date: dd/mm/yyyy")
        birthdate = input()
        return birthdate

    def new_player_gender(self):
        """ get the player gender """
        print("Type in player's Gender: Male /Female")
        gender = input()
        return gender

    def new_player_rank(self):
        """ get the player rank """
        print("Type in player's rank:")
        rank = int(input())
        return rank

    def new_player_score(self):
        """ get the player score """
        print("Type in player's score:")
        score = int(input())
        return score

    def player_list(self, player):
        """ give the list of the players """

        print("---------------------------------")
        print("Last_name:", player["Last_name"])
        print("First_name:", player["First_name"])
        print("Birth_date:", player["Birth_date"])
        print("Gender:", player["Gender"])
        print("Rank:", player["Rank"])
        print("Score:", player["Score"])
        print("---------------------------------")

    def player_search(self, player):
        """ show the searched players """

        print("-------Your research result------------")
        print("doc_id:", player.doc_id)
        print("Last_name:", player["Last_name"])
        print("First_name:", player["First_name"])
        print("Birth_date:", player["Birth_date"])
        print("Gender:", player["Gender"])
        print("Rank:", player["Rank"])
        print("Score:", player["Score"])
        print("---------------------------------------")

    # Tournament Menu
    def menu_tournament(self):
        """ print the Tournament menu """
        print("----------- Tournament Menu -----------")
        print("Please select your action and press Enter")
        print("1.Create a Tournament")
        print("2.Edit a Tournament")
        print("3.List of Tournaments")
        print("4.Add a player in Tournament")
        print("5.Return to Main menu")
        print("---------------------------------------")

    def new_tournament_name(self):
        """ get the tournament name"""
        print("Type in Tournament's name: ")
        name = input()
        return name

    def new_tournament_location(self):
        """ get the tournament location"""
        print("Type in Tournament's location: ")
        location = input()
        return location

    def new_tournament_date(self):
        """ get the tournament date"""
        print("Type in Tournament's date: dd/mm/yyyy ")
        tournament_date = input()
        return tournament_date

    def new_tournament_timer(self):
        """ get the tournament timer"""
        print("Type in tournament's timer: ")
        timer = input()
        return timer

    def new_tournament_description(self):
        """ get the tournament location"""
        print("Type in Tournament's description: ")
        description = input()
        return description

    def tournament_list(self, tournament):
        """ give the list of the tournaments"""

        print("------- Tounament's list -------")
        print("doc_id:", tournament.doc_id)
        print("Tournament_name:", tournament["Tournament_name"])
        print("Tournament_location:", tournament["Tournament_location"])
        print("Tournament_start_date:", tournament["Tournament_start_date"])
        print("Tournament_end_date:", tournament["Tournament_end_date"])
        print("Tournament_rondes:", tournament["Tournament_rondes"])
        print("Tournament_tournees:", tournament["Tournament_tournees"])
        print("Tournament_players:", tournament["Tournament_players"])
        print("Tournament_Tcontrol:", tournament["Tournament_Tcontrol"])
        print("Tournament_description:", tournament["Tournament_description"])
        print("---------------------------------")

    def tournament_load(self, tournament):
        """ give the list of the tournament"""

        print("-------- Données du tournoi chargé ---------")
        print("Tournament_name:", tournament.name)
        print("Tournament_location:", tournament.location)
        print("Tournament_start_date:", tournament.start_date)
        print("Tournament_end_date:", tournament.end_date)
        print("Tournament_rondes:", tournament.rondes)
        print("Tournament_tournees:", tournament.tournees_list)
        print("Tournament_players:", tournament.tt_players)
        print("Tournament_Tcontrol:", tournament.time_control)
        print("Tournament_description:", tournament.description)
        print("--------------------------------------------")

    def add_player(self):
        """ get the tournament name"""
        print("Please add 8 players in your tournament")

    def add_player_confirm(self):
        """ get the tournament name """
        print("Confirm player ? y/n ")

    # Report Menu

    def menu_report(self):
        """ print the report menu """

        print("------------ Report Menu -------------")
        print("welcome, please select your action and press Enter")
        print("List of all players:")
        print("    1. Alphabetical order")
        print("    2. Ranking order")
        print("List of all players for one tournament:")
        print("    3. Alphabetical order")
        print("    4. Ranking order")
        print("5.List of all tournaments")
        print("6.List of all rounds in a tournament")
        print("7.List of all matchs in a tournament")
        print("8.Return to start menu")
        print("--------------------------------------")

    # Round menu
    
    def start_view(self):
        """ start tournament view """
        print("Select tournament time control: 1- Bullet, 2-Blitz, 3-")

    def f_round(self, p, c):
        """ shows the player vs player view"""
        print("----- Round players ranking-----")
        for i in range(4):
            print(
                "Player:",
                p[i].lastname,
                p[i].rank,
                "vs",
                "Player:",
                c[i].lastname,
                c[i].rank,
            )

    def first_round(self, p, c):
        """ view to set the winner"""
        print("--------- Choose the winner or draw -----------")
        for i in range(4):
            print("Winner:", p[i].lastname, "[1]", "or", c[i].lastname, "[2]")
            print("Draw: [3)")
        print("The round is over, enter results:")

    def new_round(self):
        """ view to choose to start a new round"""
        print("Start the round? y/n")

    def other_round(self, player):
        """ view of the player list for the score management """
        print("----- Round players ranking-----")
        for i in range(0, len(player), 2):
            print(
                "Player:",
                player[i].lastname,
                player[i].score,
                "vs",
                "Player:",
                player[i + 1].lastname,
                player[i + 1].score,
            )
        print("------------------------------------")

    def oth_round(self, player):
        """ view for choose the winner """
        print("--------- Choose the winner or draw -----------")
        for i in range(0, len(player), 2):
            print(
                "Winner:",
                player[i].lastname,
                "[1]",
                "or",
                player[i + 1].lastname,
                "[2]",
            )
            print("Draw: [3)")
        print("The round is finish, enter results:")

    def round_view(self, rounds):
        """ view all rounds for a tournament"""
        print("---------------------------------")
        print("Round:", rounds["Round"])
        print("Start_time:", rounds["Start_time"])
        print("End_time:", rounds["End_time"])
        print("Matchs:", rounds["Matchs"])
        print("---------------------------------")

    def match_view(self, match):
        """ viaw all matches of the tournament """
        print("Matchs:", match["Matchs"])

    def end_tournament(self, player):
        """ view whit the players results of the tournament"""
        print("----- End of the tournament - players ranking-----")
        for i in range(0, len(player), 2):
            print(
                "Player:",
                player[i].lastname,
                player[i].score,
                "vs",
                "Player:",
                player[i + 1].lastname,
                player[i + 1].score,
            )
        print("-------------------------------------------------------")
