
class Player:
    '''
    Player's class. It allows the creation of a player, based on the attributes of the __init__(self) method
    The model should also allow to update, read and delete data from the Player's table
    '''

    def __init__(self, name, first_name, birthdate, gender, rank, score=0):
        """ initialize a player object """
        self.name = name
        self.first_name = first_name
        self.birthdate = birthdate
        self.gender = gender
        self.rank = rank
        self.score = score

    def __str__(self):
        """ display player's infos """
        info = f'name : {self.name} -- rank : {self.rank} -- score : {self.score}'
        return info.format(self)

    def serialize_player(self):
        """" serialize player's info for TinyDB """
        serialized_player = {
            "Last_name": self.name,
            "First_name": self.first_name,
            "Birthdate": self.birthdate,
            "Gender": self.gender,
            "Rank": self.rank,
            "Score": self.score,
        }
        return serialized_player

    def deserialize_player(cls, player):
        """ deserialize player table from TinyDB"""
        lastname = player["Last_name"]
        firstname = player["First_name"]
        birth_date = player["Birthdate"]
        gender = player["Gender"]
        rank = player["Rank"]
        score = player["Score"]
        player = Player(lastname, firstname, birth_date, gender, rank, score)
        return player


class Tournament:
    '''
    Tournament's class. It allows the creation of a new tournament, based on the attributes of the __init__(self) method
    The model should also allow to update, read and delete data from the Tournament's table
    It is fed with rounds and players' info
    '''

    def __init__(self, name, location, tournament_date, rounds_number, rounds_list, players_list, timer, description):
        """ initialize a tournament object """
        self.name = name
        self.location = location
        self.tournament_date = tournament_date
        self.rounds_number = rounds_number
        self.rounds_list = rounds_list
        self.players_list = players_list
        self.timer = timer
        self.description = description

    def __str__(self):
        """ display tournament's infos """
        info = f'name : {self.name} -- location : {self.location} -- rounds  : {self.rounds} -- timer : {self.timer} -- description : {self.description}'
        return info.format(self)

    def add_players(self, player):
        """ add a player to the player's list """
        self.players_list.append(player)

    def add_round(self, round):
        """ add all the rounds in the round's list """
        self.rounds_list.append(round)

    def serialize_tournament(self):
        """" serialize tournament's infos for TinyDB """
        serialized_tournament = {
            "Tournament_name": self.name,
            "Tournament_location": self.location,
            "Tournament_date": self.tournament_date,
            "Tournament_rounds_number": self.rounds_number,
            "Tournament_rounds_list": self.rounds_list,
            "Tournament_players": self.players_list,
            "Tournament_timer": self.timer,
            "Tournament_description": self.description,
        }
        return serialized_tournament

    def deserialize_tournament(cls, tournament):
        """ deserialize tournament table from TinyDB """
        name = tournament["Tournament_name"]
        location = tournament["Tournament_location"]
        tournament_date = tournament["Tournament_date"]
        rounds_number = tournament["Tournament_rounds_number"]
        rounds_list = tournament["Tournament_rounds_list"]
        players_list = tournament["Tournament_players"]
        timer = tournament["Tournament_timer"]
        description = tournament["Tournament_description"]
        tournament = Tournament(
            name, location, tournament_date, rounds_number, rounds_list, players_list, timer, description
        )
        return tournament


class Round:
    '''
    Round's class. It allows the creation of a new round, based on the attributes of the __init__(self) method
    The model should also allow to update, read and delete data from the Round's table
    It is fed with matches and players' info
    '''

    def __init__(self, round_name, start_date_time, end_date_time, match_list=[]):
        self.round_name = round_name
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time
        self.match_list = match_list

    def serialize_rounds(self):
        """" serialize the rounds for TinyDB """
        serialized_rounds = {
            "Round_name": self.round_name,
            "Start_time": self.start_date_time,
            "End_time": self.end_date_time,
            "Matchs": self.match_list,
        }
        return serialized_rounds

    def deserialize_rounds(cls, rounds):
        """ deserialize rounds table from TinyDB """
        round_name = rounds["Round_name"]
        start_date_time = rounds["Start_time"]
        end_date_time = rounds["End_time"]
        match_list = rounds["Matchs"]
        rounds = Round(round_name, start_date_time, end_date_time, match_list)
        return rounds

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

