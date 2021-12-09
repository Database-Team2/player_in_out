import pymysql
import json

with open("./in_out.json", "r", encoding="utf8") as json_file:
    contents = json_file.read()
    json_data = json.loads(contents)

conn=pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="jaesung4231@",
    database="epl",
    charset = "utf8"
)

sql_match_lineup = "insert into match_lineups(match_id, home_team_id,away_team_id,home_lineups,away_lineups) values(%s,%s,%s,%s,%s)"
sql_match_sub="insert into match_sub(match_id, home_team_id,away_team_id,home_sub,away_sub) values(%s,%s,%s,%s,%s)"
sql_match_inout="insert into in_out(match_id,in_out,time,player_id,club_id) values(%s,%s,%s,%s,%s)"
temp=[]
curs=conn.cursor()
for i in range(len(json_data["match_lineup"])):
    for j in range(len(json_data["match_lineup"][i]["Home_lineups"])):
        curs.execute(sql_match_lineup , (json_data["match_lineup"][i]["match_id"],
                       json_data["match_lineup"][i]["Home_team"],
                       json_data["match_lineup"][i]["Away_team"],
                       json_data["match_lineup"][i]["Home_lineups"][j],
                       json_data["match_lineup"][i]["Away_lineups"][j],
                      ))

for i in range(len(json_data["match_lineup"])):
    print(len(json_data["match_lineup"][i]["Home_sub"]))
    print(len(json_data["match_lineup"][i]["Away_sub"]))
    for j in range(9):
        if(len(json_data["match_lineup"][i]["Home_sub"])<9):
            json_data["match_lineup"][i]["Home_sub"].append(None)
        elif(len(json_data["match_lineup"][i]["Away_sub"])<9):
            json_data["match_lineup"][i]["Away_sub"].append(None)
        curs.execute(sql_match_sub,(json_data["match_lineup"][i]["match_id"],
                       json_data["match_lineup"][i]["Home_team"],
                       json_data["match_lineup"][i]["Away_team"],
                       json_data["match_lineup"][i]["Home_sub"][j],
                       json_data["match_lineup"][i]["Away_sub"][j],
                      ))    
for i in range(len(json_data["players_in_out"])):
     
       curs.execute(sql_match_inout,(
           json_data["players_in_out"][i]["match_id"],
           json_data["players_in_out"][i]["in_out"],
           json_data["players_in_out"][i]["time"],
           json_data["players_in_out"][i]["player"],
          json_data["players_in_out"][i]["club_id"]
       ))
                                      



rows=curs.fetchall()
conn.commit()
conn.close()
