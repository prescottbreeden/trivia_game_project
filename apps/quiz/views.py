from django.shortcuts import render, HttpResponse, redirect
from apps.quiz.models import *
from apps.login.models import *

# Create your views here.
def quiz(request):
	if 'user_id' not in request.session:
		return redirect('/')
	context = {'categories' : Category.objects.all()}
	return render(request, 'quiz/quiz.html', context)

def create_quiz(request, id):
	if 'user_id' not in request.session:
		return redirect('/')

	request.session['cat_id'] = id
	context = {
		'user': User.objects.get(id=request.session['user_id']),
		'questions': Quiz.objects.make_quiz(id=id)
	}
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
	return render(request, 'quiz/quiz_end.html', context)

def quiz_stats(request):
	
	return render(request, 'quiz/quiz_chart_test.html')

def make_chart (request):

	return Quiz.objects.make_chart(request.session['user_id'])