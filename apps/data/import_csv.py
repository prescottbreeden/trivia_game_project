from django.db import models
from apps.quiz.models import People
import csv

with open(athletes.csv) as csvfile:
	csv_reader = csv.DictReader(csvfile)
	for row in csv_reader: 
		People.objects.create(
			name = row['name'],
			category = Category.objects.get(id=category),
			abstract = row['abstract'],
			)
