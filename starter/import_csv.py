import csv

with open(athletes.csv) as csvfile:
	csv_reader = csv.DictReader(csvfile)
		for row in csv_reader: 
			Athlete.objects.create(
				name = row['name'],
				category = Category.objects.get(id=category),
				abstract = row['abstract'],
				)
