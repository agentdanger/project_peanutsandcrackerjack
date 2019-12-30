#!/usr/bin/env python
# coding: utf-8
from sqlalchemy import create_engine
import psycopg2
import os
import pandas as pd

user_name = input("What is your user id?")
password = input("What is your password?")

db = create_engine('postgresql://{0}:{1}@localhost:5433/baseballdatabank'.format(user_name, password))

conn = psycopg2.connect(dbname='baseballdatabank', 
                        host='localhost',  
                        user='{}'.format(user_name),
                        port='5433',
                        password='{}'.format(password)
                       )

os.chdir(r"C:\Users\Courtney Perigo\Documents\GitHub\baseballdatabank\core")

HallofFame = pd.read_csv("HallofFame.csv")
Appearances = pd.read_csv("Appearances.csv")
AwardsPlayers = pd.read_csv("AwardsPlayers.csv")
Batting = pd.read_csv("Batting.csv")
Fielding = pd.read_csv("Fielding.csv")
Managers = pd.read_csv("Managers.csv")
Parks = pd.read_csv("Parks.csv")
People = pd.read_csv("People.csv")
Pitching = pd.read_csv("Pitching.csv")
Salaries = pd.read_csv("Salaries.csv")
Schools = pd.read_csv("Schools.csv")
Teams = pd.read_csv("Teams.csv")
Teamsfranchises = pd.read_csv("Teamsfranchises.csv")

cur = conn.cursor()
cur.execute('DROP VIEW "v_player_batting_majors";')
conn.commit()

HallofFame.to_sql('halloffame', con=db, if_exists='replace', index_label='id')
Appearances.to_sql('appearances', con=db, if_exists='replace', index_label='id')
AwardsPlayers.to_sql('awardsplayers', con=db, if_exists='replace', index_label='id')
Batting.to_sql('batting', con=db, if_exists='replace', index_label='id')
Fielding.to_sql('fielding', con=db, if_exists='replace', index_label='id')
Managers.to_sql('managers', con=db, if_exists='replace', index_label='id')
Parks.to_sql('parks', con=db, if_exists='replace', index_label='id')
People.to_sql('people', con=db, if_exists='replace', index_label='id')
Pitching.to_sql('pitching', con=db, if_exists='replace', index_label='id')
Salaries.to_sql('salaries', con=db, if_exists='replace', index_label='id')
Schools.to_sql('schools', con=db, if_exists='replace', index_label='id')
Teams.to_sql('teams', con=db, if_exists='replace', index_label='id')
Teamsfranchises.to_sql('teamsfranchises', con=db, if_exists='replace', index_label='id')

cur.execute("""
CREATE VIEW v_player_batting_majors AS
SELECT pe."playerID",
max(pe."nameFirst"::text) AS namefirst,
max(pe."nameLast"::text) AS namelast,
max(pe."nameGiven"::text) AS namegiven,
sum(ba_p."AB") AS ab,
sum(ba_p."R") AS r,
sum(ba_p."H") AS h,
sum(ba_p."2B") AS "b_2B",
sum(ba_p."3B") AS "b_3B",
sum(ba_p."HR") AS hr,
sum(ba_p."RBI") AS rbi,
sum(ba_p."SB") AS sb,
sum(ba_p."CS") AS cs,
sum(ba_p."BB") AS bb,
sum(ba_p."SO") AS so,
sum(ba_p."IBB") AS ibb,
sum(ba_p."HBP") AS hbp,
sum(ba_p."SH") AS sh,
sum(ba_p."SF") AS sf,
sum(ba_p."GIDP") AS gidp
FROM batting ba_p
LEFT JOIN people pe ON pe."playerID"::text = ba_p."playerID"::text
WHERE ba_p."lgID"::text ~~ 'NL'::text OR ba_p."lgID"::text ~~ 'AL'::text
GROUP BY pe."playerID";
""")
conn.commit()
cur.close()