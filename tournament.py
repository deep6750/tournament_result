#!/usr/bin/env python

# tournament.py -- implementation of a Swiss-system tournament


import psycopg2

# Connect PSQL database to tournament database.
# DataBase Name :- tournament


def connect():
    database = psycopg2.connect("dbname=tournament")
    return database


# Returns the number of players currently registered.

def countPlayers():
    db = connect()
    cur = db.cursor()
    cur.execute("SELECT count(common_id) FROM tournament_Players;")
    tuples = cur.fetchall()
    db.close()
    return tuples[0][0]

# commit player to the database :- tournament

def registerPlayer(player_name):
    """
    Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
    player_name: the player's full name (need not be unique).
    """
    db = connect()
    cur = db.cursor()
    cur.execute("INSERT INTO tournament_Players (player_name) VALUES (%s)", (player_name,))
    db.commit()
    db.close()

# Returns a sorted list of the players and their win records from standings view.

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.
    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.
    Returns:
      A list of tuples, each of which contains (common_id, player_name, wins, matches):
        common_id: the player's unique id (assigned by the database)
        Player_name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db = connect()
    cur = db.cursor()
    cur.execute("SELECT common_id,player_name,wins,matches FROM Standings ORDER BY wins DESC;")
    tuples = cur.fetchall()
    db.close()
    return tuples

# Remove all record from database of match table.


def deleteMatches():
    db = connect()
    cur = db.cursor()
    cur.execute("DELETE FROM tournament_Matches")
    db.commit()
    db.close()

 # Remove all record from database of player table.


def deletePlayers():
    db = connect()
    cur = db.cursor()
    cur.execute("DELETE FROM tournament_Players")
    db.commit()
    db.close()




# Records the output of a single match between two players.

def reportMatch(winner, loser, make):
    """Records the outcome of a single match between two players.
    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db = connect()
    cur = db.cursor()
    if make:
        cur.execute(
            "INSERT INTO tournament_Matches (winner,looser,result) VALUES (%s,%s,1)",
            (winner,
             loser))
        cur.execute(
            "INSERT INTO tournament_Matches (winner,looser,result) VALUES (%s,%s,1)",
            (loser,
             winner))
    else:
        cur.execute(
            "INSERT INTO tournament_Matches (winner,looser,result) VALUES (%s,%s,1)",
            (winner,
             loser))
        cur.execute(
            "INSERT INTO tournament_Matches (winner,looser,result) VALUES (%s,%s,0)",
            (loser,
             winner))
    db.commit()
    db.close()



# Returns a list of pairs of players for the next round of a match.
    
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    db = connect()
    cur = db.cursor()
    cur.execute("SELECT common_id,player_name,wins FROM Standings ORDER BY wins DESC;")
    tuples = cur.fetchall()
    db.close()
    i = 0
    combination = []
    while i < len(tuples):
        player_one_id = tuples[i][0]
        player_two_id = tuples[i + 1][0]
        player_one_name = tuples[i][1]
        player_two_name = tuples[i + 1][1]
        combination.append((player_one_id, player_one_name, player_two_id, player_two_name))
        i = i + 2
    return combination
