import csv

class Athlete:
	def __init__(self, sport, name, abstract):
		self.sport = sport
		self.name = name
		self.abstract = abstract				

	def populate_athletes(file):
		with open(file) as csvfile:
			csv_reader = csv.DictReader(csvfile)
			for row in csv_reader: 
				self.sport = sport
				self.name = row['name']
				self.abstract = row['abstract']
