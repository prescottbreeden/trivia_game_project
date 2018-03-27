			#For Loop suffles the list of people that fit the catagory into a random order
			for i in range (0,len(people_list)):
				temp = people_list[i]
				random_index = randint(0, len(people_list))-1
				temp2 = people_list[random_index]
				people_list[random_index] = temp
				people_list[i] = temp2

{'questions': 
	{
	'trivia': 'Former American football star... "', 
	'answer_list': 
		[
		{'answer': {
			'athlete': <Quiz object: Ernie Davis}, 
			'value': False
			}, 
		{'answer': {
			'athlete': <Quiz object: O.J. Simpson}, 
			'value': True
			}, 
		{'answer': {
			'athlete': <Quiz object: Tim Tebow}, 
			'value': False
			}, 
		{'answer': {
			'athlete': <Quiz object: Nick Foles}, 
			'value': False
			}
		]
	}
}

