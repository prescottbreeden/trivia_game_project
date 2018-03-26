import requests
from bs4 import BeautifulSoup
from time import sleep
from csv import writer, DictWriter
from random import choice

all_questions = []
base_url = 'http://trivia.fyi'
url = '/category/sports-trivia?page=1'

while url:
	res = requests.get(f'{base_url}{url}')
	print(f'Now Scraping {url}...')
	soup = BeautifulSoup(res.text, 'html.parser')
	question = soup.find(class_="title").get_text()
	answer = soup.find(class_="spoiler-content").get_text()

	next_btn = soup.find(class_='pager-next')
	url = next_btn.find('a')['href'] if next_btn else None
	sleep(3)

	all_questions.append({
			'category': 'general',
			'question': question,
			'answer': answer
			})

with open("general_trivia.csv", "w") as file:
		headers = ["Category", "Question", "Answer"]
		csv_writer = writer(file)
		csv_writer.writerow(headers)
		for question in all_questions:
			row = (question['category'], question['question'], question['answer'])
			csv_writer.writerow(row)
	