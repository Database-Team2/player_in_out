import pymysql
import json

with open("./match_line_up_id.json", "r", encoding="utf8") as json_file:
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

sql_home_lineup = "insert into home_lineup(match_id, home_team_id, home_lineups_id) values(%s,%s,%s)"
sql_home_sub="insert into home_sub(match_id, home_team_id, home_sub_id) values(%s,%s,%s)"
sql_away_lineup = "insert into away_lineup(match_id, away_team_id, away_lineup_id) values(%s,%s,%s)"
sql_away_sub = "insert into away_sub(match_id, away_team_id, away_sub_id) values(%s,%s,%s)"


temp=[]
curs=conn.cursor()
for i in range(len(json_data["match_lineup"])):
    for j in range(len(json_data["match_lineup"][i]["Home_lineups"])):
        curs.execute(sql_home_lineup , (json_data["match_lineup"][i]["match_id"],
                       json_data["match_lineup"][i]["Home_team"],
                       json_data["match_lineup"][i]["Home_lineups"][j],
                      ))


for i in range(len(json_data["match_lineup"])):
    for j in range(len(json_data["match_lineup"][i]["Home_sub"])):
        curs.execute(sql_home_sub ,(json_data["match_lineup"][i]["match_id"],
                       json_data["match_lineup"][i]["Home_team"],
                       json_data["match_lineup"][i]["Home_sub"][j],
                      ))


for i in range(len(json_data["match_lineup"])):
    for j in range(len(json_data["match_lineup"][i]["Away_lineups"])):
        curs.execute(sql_away_lineup , (json_data["match_lineup"][i]["match_id"],
                       json_data["match_lineup"][i]["Away_team"],
                       json_data["match_lineup"][i]["Away_lineups"][j],
                      ))

for i in range(len(json_data["match_lineup"])):
    for j in range(len(json_data["match_lineup"][i]["Away_sub"])):
        curs.execute(sql_away_sub ,(json_data["match_lineup"][i]["match_id"],
                       json_data["match_lineup"][i]["Away_team"],
                       json_data["match_lineup"][i]["Away_sub"][j],
                      ))

rows=curs.fetchall()
conn.commit()
conn.close()
