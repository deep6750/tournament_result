-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- CREATE DATABASE FOR STORING TOURNAMENT DATA
CREATE DATABASE tournament;
-- CONNECT TO DATABASE
\c tournament

-- Table for Players
CREATE TABLE tournament_Players (
	common_id SERIAL primary key,
	player_name varchar(255)
);

-- Table for Matches
CREATE TABLE tournament_Matches (
	common_id SERIAL primary key,
	winner int references tournament_Players(common_id),
	looser int references tournament_Players(common_id),
	result int
);

-- for each player it show the number of wins from won view
CREATE VIEW Won AS
	SELECT tournament_Players.common_id, COUNT(tournament_Matches.looser) AS no 
	FROM tournament_Players
	LEFT JOIN (SELECT * FROM tournament_Matches WHERE result>0) as tournament_Matches
	ON tournament_Players.common_id = tournament_Matches.winner
	GROUP BY tournament_Players.common_id;

-- Count View shows number of matches for each Player
CREATE VIEW Match_Count AS
	SELECT tournament_Players.common_id, COUNT(tournament_Matches.looser) AS no 
	FROM tournament_Players
	LEFT JOIN tournament_Matches
	ON tournament_Players.common_id = tournament_Matches.winner
	GROUP BY tournament_Players.common_id;

-- Standings View shows number of wins matches and matches for every Player
CREATE VIEW Standings AS 
	SELECT tournament_Players.common_id,tournament_Players.player_name,Won.no as wins,Match_Count.no as matches 
	FROM tournament_Players,Match_Count,Won
	WHERE tournament_Players.common_id = Won.common_id and Won.common_id = Match_Count.common_id;