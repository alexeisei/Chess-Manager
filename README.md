# Chess-Manager

An offline application that allows the management of a Swiss' rules based chess tournament.

It is based on a Model View Controller system to allow a clear and easily maintainable code.

It allows to :
- create new tournaments with informations as location, name, date, description
- create players profiles with informations such as name, gender, age, rank
- serialize and stock these informations in Json files 
- deserialize them into the application 
- generate reports about previously played tournaments, player's database, rounds and matches played in a previous tournament

The user can then create a new tournament, add 8 players to it and manage a full tournament following the swiss' rules.

The application generates automatically the match making by itself.

The user enters the winners at the end of each round (4 matches each). 
The application will then give the results of the tournament at the end of the 4th round.


## To use the application

1) Download the Zip files from this page and unzip them in the directory of your choice
2) Launch the command prompt on your system and go to the directory you unzipped the files
3) type in the following commands to create a virtual environement :

```
python -m venv env
```
For Linux or Mac
```
-env\Scripts\activate.bat
```
Or for Windows :
```
env\Scripts\activate
```
```
pip install -r requirements.txt
```




To generate flake8 reports :

flake8 --max-line-length=119 --format=html --htmldir=html-report --exclude=__pycache__,env,venv
