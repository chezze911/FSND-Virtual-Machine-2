--Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.

DROP DATABASE tournament;
CREATE DATABASE tournament;


CREATE TABLE players  (id serial PRIMARY KEY,
                        name text);

CREATE TABLE matches  (id serial PRIMARY KEY,
                        winner_id int,
                        loser_id int,
                        FOREIGN KEY (winner_id) REFERENCES players(id),
                        FOREIGN KEY (loser_id) REFERENCES players(id));


-- Command
-- Description
-- Usage
-- Action
-- psql
-- launches the psql command line interface
-- psql tournament
-- launches and connects to tournament database
-- \c
-- connect
-- \c tournament
-- connects to the tournament database, drops connection to previous database
-- \i
-- import
-- \i tournament.sql
-- executes the sql commands within the sql file from psql
-- \?
-- help
-- \?
-- get help with psql commands
-- \q
-- quit
-- \q
-- quit the psql command line interface
-- \d
-- describe
-- \d matches
-- describes the table structure
-- \dt
-- list tables
-- \dt
-- list tables in current database