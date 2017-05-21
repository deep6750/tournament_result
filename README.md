# Tournament Result

A a database schema to store the game matches between players and to query this data and determine the winners of each and every game

# How to Run:
Clone or Download this Repository
1. First install vagrant from https://www.vagrantup.com/downloads.html
2. Then go to the project directory where Vagrantfile is present
3. Then right click and open terminal and type following commands:-
* vagrant up && vagrant ssh
* cd /vagrant
* Then you have to install python pip :- sudo apt-get install python-pip
* Then install PostgreSQL :- sudo pip install psycopg2
* Then load database :- psql -f tournament.sql
* Then Run :- python tournament_test.py

## This will be the output
1. Old matches can be deleted.
2. Player records can be deleted.
3. After deleting, countPlayers() returns zero.
4. After registering a player, countPlayers() returns 1.
5. Players can be registered and deleted.
6. Newly registered players appear in the standings with no matches.
7. After a match, players have updated standings.
8. After one match, players with one win are paired.
 Success!  All tests pass!


