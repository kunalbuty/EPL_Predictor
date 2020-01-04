#!/usr/bin/python3

import requests
import mysql.connector
from bs4 import BeautifulSoup

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="EPL_Predictor"

)
print(mydb)

fifas=["07","08","09","10","11"]
mycursor = mydb.cursor()
sql="INSERT INTO Team_Stats (Team_Name, Attack, Midfield, Defense, FIFA_Version) VALUES (%s,%s,%s,%s,%s)"

for fifa in fifas:

	url="https://www.fifaindex.com/teams/fifa"+fifa+"/?league=13&order=desc"
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')

	table = soup.find('table', class_='table table-striped table-teams').find('tbody')
	teams= table.find_all('tr',{'class': None})
	counter=0
	for team in teams:
		if counter>0:
			teamName=team.find("td", {"data-title" : "Name"}).find('a').text.strip()
			attack=int(team.find("td", {"data-title" : "ATT"}).find('span').text.strip())
			midfield=int(team.find("td", {"data-title" : "MID"}).find('span').text.strip())
			defense=int(team.find("td", {"data-title" : "DEF"}).find('span').text.strip())
			print(teamName," -- ATT:",attack,"--, MID:", midfield, "--, DEF:",defense,"FIFA: ",fifa)
			
			val=(teamName,attack,midfield,defense,fifa)
			mycursor.execute(sql, val)
			mydb.commit()
		
		counter=counter+1
		if counter>5:
			counter=0
			
