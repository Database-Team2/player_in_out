create table match_lineups(
    match_id int,
    home_team_id int,
    away_team_id int,
    home_lineups int,
    away_lineups int,
	foreign key(match_id) references match_info(match_id)
);
create table match_sub(
	match_id int,
    home_team_id int,
    away_team_id int,
    home_sub int,
    away_sub int,
	foreign key(match_id) references match_info(match_id)
);
create table in_out(
    match_id int,
    in_out varchar(20),
    time varchar(10),
    player_id int,
    club_id int,
    foreign key(match_id) references match_info(match_id)
)








create table in_out(
	match_id int,
    in_out varchar(20),
    time varchar(20),
    player_id int,
    club_id int,
    foreign key(match_id) references match_info(match_id)
)






