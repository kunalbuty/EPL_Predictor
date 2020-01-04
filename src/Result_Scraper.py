#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup

url="https://www.skysports.com/premier-league-results/2006-07"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find_all('div', class_='fixres__item')
team1=""
team2=""
for i in results:
	teams=i.find_all('span',class_="swap-text__target")
	#name1=team1.find_all('span',class_="swap-text__target")
	counter=0;
	for team in teams:
		if counter==0:
			counter=counter+1
			team1=team.text
		else:
			counter=0
			team2=team.text
	print(team1," vs ",team2)