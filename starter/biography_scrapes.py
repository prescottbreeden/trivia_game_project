import requests
from bs4 import BeautifulSoup
from time import sleep
from csv import writer, DictWriter
from random import choice

all_athletes = []
all_urls = [
	{'url': 'people/groups/football-players'},
	{'url': 'people/groups/athletes-soccer-players'},
	{'url': 'people/groups/athletes-baseball-players'},
	{'url': 'people/groups/athletes-basketball-players'},
	{'url': 'people/groups/athletes-hockey-players'},
	{'url': 'people/groups/athletes-boxers'},
	{'url': 'people/groups/athletes-golfers'},
	{'url': 'people/groups/athletes-martial-arts-experts'},
	{'url': 'people/groups/athletes-tennis-players'},
]
base_url = 'https://www.biography.com/'
for page in all_urls:
	url = page['url']
	res = requests.get(f'{base_url}{url}')
	print(f'Now Scraping {url}...')
	soup = BeautifulSoup(res.text, 'html.parser')
	people = soup.find_all(class_="m-card--label")
	for person in people:
		person_href = person.contents[0]['href']
		if person_href == '/people/michael-sam':
			continue;
		person_res = requests.get(f'{base_url}{person_href}')
		print(f'Now Scraping {person_href}...')
		person_soup = BeautifulSoup(person_res.text, 'html.parser')
		person_name = person_soup.find('dd').get_text()
		person_abstract = person_soup.find(class_='l-person--abstract').get_text()
		all_athletes.append({
			'category': url.split('/')[-1:][0],
			'name': person_name,
			'abstract': person_abstract
			})
		sleep(3)
	with open("athletes.csv", "w") as file:
		headers = ["Category", "Name", "Abstract"]
		csv_writer = writer(file)
		csv_writer.writerow(headers)
		for athlete in all_athletes:
			row = (athlete['category'], athlete['name'], athlete['abstract'])
			csv_writer.writerow(row)