#import datetime


class Player:
    '''
    Player's class. It allows the creation of a player, based on the attributes of the __init__(self) method
    The model should also allow to update, read and delete data from the Player's table
    '''

    def __init__(self, name, first_name, birthdate, gender, rank, score=0):
        self.name = name
        self.first_name = first_name
        self.birthdate = birthdate
        self.gender = gender
        self.rank = rank
        self.score = score

    def __str__(self):
        info = f'name : {self.name} -- rank : {self.rank} -- score : {self.score}'
        return info.format(self)

    def to_dict(self):
        player_dict = {"name": self.name,
                       "first_name": self.first_name,
                       "birthday": str(self.birthdate),
                       "gender": self.gender,
                       "rank": self.rank}

        return player_dict


class Tournament:
    '''
    Tournament's class. It allows the creation of a new tournament, based on the attributes of the __init__(self) method
    The model should also allow to update, read and delete data from the Tournament's table
    It is fed with rounds and players' info
    '''

    def __init__(self, name, location, tournament_date, rounds_number, round_list, players_list, timer, description):
        self.name = name
        self.location = location
        self.tournament_date = datetime.date.today().strftime("%d/%m/%Y")
        self.rounds_number = rounds_number#4
        self.round_list = []#liste des instances de round
        self.players_list = []#liste des instances de joueurs
        self.timer = timer
        self.description = description

    def __str__(self):
        info = f'name : {self.name} -- location : {self.location} -- rounds  : {self.rounds} -- timer : {self.timer} -- description : {self.description}'
        return info.format(self)

    def add_players(self, player):
        self.players_list.append(player)

    def add_round(self, round):
        self.round_list.append(round)

    def to_dict(self):
        tournament_dict = {
            "Name": self.name,
            "Location": self.location,
            "Rounds": self.rounds,
            "Round_list": self.round_list,
            "Players_list": self.players_list,
            "Timer": self.timer,
            "Description": self.description
        }
        #for matches in self.round_list:
        #    tournament_dict["round_list"].append(matches.to_dictionary())

        return tournament_dict


class Round:
    '''
    Round's class. It allows the creation of a new round, based on the attributes of the __init__(self) method
    The model should also allow to update, read and delete data from the Round's table
    It is fed with matches and players' info
    '''

    def __init__(self, round_name, start_date_time, end_date_time, match_list=[], match_results=[]):
        self.round_name = round_name
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time
        self.match_list = match_list
        self.match_results = match_results

    def add_match(self, match):
        self.match_list.append(match)

    def add_results(self, results):
        self.match_results.append(results)


class Match:
    '''
    Match's class. It allows the creation of a new match, based on the attributes of the __init__(self) method
    The model should also allow to update, read and delete data from the Match's table
    It is fed with the results of the match and players' info
    '''

    def __init__(self, player1, player2, player1_score=0, player2_score=0):
        self.player1 = player1
        self.player2 = player2
        self.player1_score = player1_score
        self.player2_score = player2_score

    def won_match(self):
        self.score += 1.0

    def draw_match(self):
        self.score += 0.5

    #def set_winner(self, winner):
        #self.winner = winner

    def to_dictionary(self):
         match_dict = {
            "Player 1 name : ": self.player1,
            "Player 2 name : ": self.player2,
            "Player 1 score : ": self.player1_score,
            "Player 2 score : ": self.player2_score
            }

         return match_dict
    #tuple contenant deux listes, chacune contenant deux éléments : ((joueur1, score1) + (joueur2, score2))  ([], [])
	#une référence à une instance de joueur
	#un score

