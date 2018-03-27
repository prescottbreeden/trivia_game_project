			#For Loop suffles the list of people that fit the catagory into a random order
			for i in range (0,len(people_list)):
				temp = people_list[i]
				random_index = randint(0, len(people_list))-1
				temp2 = people_list[random_index]
				people_list[random_index] = temp
				people_list[i] = temp2

{'questions': 
	{
	'category': 1
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

path('submit/<str:answer>', views.submit_quiz, name = 'submit_quiz'),

def submit_quiz(request, answer):
	
	if answer == Question.answer:
		score = 1
	else:
		score = 0
	
	Quiz.objects.create(
		score = score,
		user = User.objects.get(id=request.session['user_id']),
		category = Category.objects.get(id = request.session['cat_id']),
		)
