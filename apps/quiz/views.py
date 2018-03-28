from django.shortcuts import render, HttpResponse, redirect
from apps.quiz.models import *
from apps.login.models import *

def quiz(request):
	if 'user_id' not in request.session:
		return redirect('/')
	context = {'categories' : Category.objects.all()}
	return render(request, 'quiz/quiz.html', context)

def create_quiz(request, id):
	if 'user_id' not in request.session:
		return redirect('/')
	request.session['cat_id'] = id
	if 'dont_repeat' not in request.session:
		request.session['dont_repeat'] = []
	trivia = Quiz.objects.make_quiz(id=id, dont_repeat = request.session['dont_repeat'])
	context = {
		'user': User.objects.get(id=request.session['user_id']),
		'questions': trivia['quiz']
	}
	request.session['dont_repeat'] = trivia['dont_repeat']
	print(request.session['dont_repeat'])
	return render(request, 'quiz/take_quiz.html', context)

def submit_quiz(request, id):
	if 'user_id' not in request.session:
		return redirect('/')
	if 'score' not in request.session:
		request.session['score'] = 0
	Quiz.objects.create(
		score = id,
		user = User.objects.get(id=request.session['user_id']),
		category = Category.objects.get(id = request.session['cat_id']),
		)
	request.session['score'] += 1

	if 'quiz_counter' not in request.session:
		request.session['quiz_counter'] = 0
	if request.session['quiz_counter'] < 5:
		request.session['quiz_counter']+=1
		return redirect('/quiz/' + str(request.session['cat_id']))
	request.session['score'] = 0
	request.session['quiz_counter'] = 0
	return redirect('/quiz/end')

def quiz_end(request):
	context = {
		'user': User.objects.get(id=request.session['user_id']),
	}
	request.session['dont_repeat'] = []
	return render(request, 'quiz/quiz_end.html', context)