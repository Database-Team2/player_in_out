create table match_info(
 match_id int primary KEY,
 match_date varchar(40),
 home_club_id int,
 away_club_id int
);
create table home_lineup(
	match_id int,
    home_team_id int,
    home_lineups_id int,
    foreign key(match_id) references match_info(match_id)
);
create table home_sub(
	match_id int,
    home_team_id int,
    home_sub_id int,
    foreign key(match_id) references match_info(match_id) 
);
create table away_lineup(
	match_id int,
    away_team_id int,
    away_lineup_id int,
    foreign key(match_id) references match_info(match_id) 
);
create table away_sub(
	match_id int,
    away_team_id int,
    away_sub_id int,
    foreign key(match_id) references match_info(match_id) 
);















