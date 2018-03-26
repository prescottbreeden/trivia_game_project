import csv

class Athlete:
	def __init__(self, category, name, abstract):
		self.category = category
		self.name = name
		self.abstract = abstract				

	def populate_athletes(file):
		with open(file) as csvfile:
			csv_reader = csv.DictReader(csvfile)
			for row in csv_reader: 
				self.category = category
				self.name = row['name']
				self.abstract = row['abstract']
