#!/usr/bin/env python
"""
tournament.py -- implementation of a Swiss-system tournament
"""

import psycopg2

def connect():
    """
    Connect to the PostgreSQL database.
    :returns: a database connection.
    """
    try:
        return psycopg2.connect("dbname=tournament")
    except:
        print("Connection failed.  Please try again")


def get_values(SQL, values=None):
    """
    SQL query to fetch values
    """
    db = connect()
    c = db.cursor()
    if values == None:
        c.execute(SQL)
    else:
        c.execute(SQL, values)
    result = c.fetchall()
    db.close()
    return result



def post_values(SQL, values=None):
    """
    The SQL query to commit
    """
    db = connect()
    c = db.cursor()
    if values == None:
        c.execute(SQL)
    else:
        c.execute(SQL, values)
    db.commit()
    db.close()


def deleteMatches():
    """
    Remove all the match records from the database.
    """
    post_values("DELETE FROM matches;")


def deletePlayers():
    """
    Remove all the player records from the database.
    """
    post_values("DELETE FROM players;")


def countPlayers():
    """
    Returns the number of players currently registered.
    """
    query = "SELECT COUNT(id) from players;"
    result = get_values(query)
    return int(result[0][0])


def registerPlayer(name):
    """
    Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    query = "INSERT INTO players (name) VALUES (%s)"
    values = (name,)
    post_values(query, values)


def playerStandings():
    """
    Returns a list of the players and their win records, sorted by wins.
    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.
    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    winners_query = "select players.id, name, count(matches.id) as wins from players left join matches on " \
                    "players.id = winner_id group by players.id order by wins desc"

    losers_query = "select players.id, count(matches.id) as losses from players left join matches on " \
                   "players.id = loser_id group by players.id order by losses desc"

    join_query = "select winners.id, winners.name, wins, wins+losses as matches from ({winners_query}) as winners left " \
                 "join ({losers_query}) as losers on winners.id = losers.id;".format(winners_query=winners_query, losers_query=losers_query)


    return get_values(join_query)


def reportMatch(winner, loser):
    """
    Records the outcome of a single match between two players.
    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    query = "INSERT INTO matches (winner_id, loser_id) VALUES ((%s), (%s))"
    values = (winner,loser)
    post_values(query, values)


def swissPairings():
    """
    Returns a list of pairs of players for the next round of a match.
  
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
    results = []

    standings = [(record[0], record[1]) for record in playerStandings()]

    # Run a for loop from index[0] to number of players in ranking skipping one index each time 
    for player_rank in range(0, len(standings), 2):
        # putting the player at index player_rank and the next one together as pairs
        results.append(standings[player_rank] + standings[player_rank + 1])
    return results
