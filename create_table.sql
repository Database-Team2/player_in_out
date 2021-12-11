create table MATCH_LINEUPS(
    match_id int unsigned not null,
    home_player_id int unsigned not null,
    away_player_id int unsigned not null,
    foreign key(match_id) references MATCH_INFO(match_id),
    foreign key(home_player_id) references PLAYER(player_id),
    foreign key(away_player_id) references PLAYER(player_id)
);
create table MATCH_SUB(
	match_id int unsigned not null, 
    home_player_id int unsigned not null,
    away_player_id int unsigned not null,
	foreign key(match_id) references MATCH_INFO(match_id),
	foreign key(home_player_id) references PLAYER(player_id),
    foreign key(away_player_id) references PLAYER(player_id)
);
create table IN_OUT(
    match_id int unsigned not null, 
    in_out varchar(20) not null,
    in_out_time char(10) not null,
    player_id int unsigned not null,
    club_id int unsigned not null,
    foreign key(match_id) references MATCH_INFO(match_id),
    foreign key(player_id) references PLAYER(player_id),
    foreign key(club_id) references CLUB_INFO(club_id)
);
create table MATCH_DETAILS(
    match_id int unsigned not null,
    home_score int unsigned not null, 
    away_score int unsigned not null, 
    home_possesion float unsigned not null, 
    away_possesion float unsigned not null, 
    home_shots_on_target int unsigned not null, 
    away_shots_on_target int unsigned not null, 
    home_shots int unsigned not null, 
    away_shots int unsigned not null, 
    King_of_the_match int unsigned not null,	
    foreign key(match_id) references MATCH_INFO(match_id),
    foreign key(King_of_the_match) references PLAYER(player_id)
)










