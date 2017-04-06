--Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.

DROP DATABASE tournament;
CREATE DATABASE tournament;
\c tournament;

CREATE TABLE players  ( 
		id serial PRIMARY KEY,
        name TEXT
);

CREATE TABLE matches  ( 
		id serial PRIMARY KEY,
        winner_id int,
        loser_id int,
        FOREIGN KEY (winner_id) REFERENCES players(id),
        FOREIGN KEY (loser_id) REFERENCES players(id) 
);


-- lists the table created
\d

-- quits the screen
\q