

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

    def add_player_confirm(self):
        """ get the tournament name """
        print("Confirm player ? y/n ")
