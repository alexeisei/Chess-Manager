# Chess-Manager

An offline application written using Python 3 that allows the management of a Swiss' rules based chess tournament.

The code is written on a Model View Controller (MVC) system to allow a clear and easily maintainable code.
It is written using the PEP8 directives.

The application allows to :
- create new tournaments with informations such as location, name, date, description
- create players' profiles with informations such as name, gender, age, rank
- serialize and stock these informations in Json files 
- deserialize them into the application from those files
- generate reports about previously played tournaments, player's database, rounds and matches played in a previous tournament

The user can then create a new tournament, add 8 players to it and manage a full tournament following the swiss' rules.

The application generates automatically the match making by itself.

The user enters the winners at the end of each round (4 matches each). 
The application will then give the results of the tournament at the end of the 4th round, with updated ranks for every player.


## To execute the application

1) Download the Zip files from this page and unzip them in the directory of your choice
2) Launch the command prompt on your system and go to the directory you unzipped the files
3) Type in the following commands to create and enable a virtual environement :
```
python -m venv env
```
For Linux or Mac :
```
-env\Scripts\activate.bat
```
Or for Windows :
```
env\Scripts\activate
```
Then for all sytems :
```
pip install -r requirements.txt
```
4) To launch the application, type in :
```
python chess.py
```

## To use the application

You can navigate the menu using the numbers corresponding to your needs and choices.

To manage a full tournament :
1) Create a new tournament
2) Create the players that will be playing in it
3) Start the tournament and add 8 players to it, the matchmaking and pairs will be generated based on the swiss' rules
4) At the end of each round, select the winner for each match
5) Repeat the process for all 4 rounds
6) At the end of the tournament, the application will show you the results with updated ranks for each player

You can generate reports to :
- see all tournaments' infos
- see all players' infos (alphabatically or by rank), for all or one specific tournament
- see the infos for one specific tournament (players' databese, list of rounds, matches, results)


## To generate flake8 reports :

Type in

```
flake8 --max-line-length=119 --format=html --htmldir=html-report --exclude=__pycache__,env,venv
```
