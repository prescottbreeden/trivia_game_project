from django.shortcuts import render, HttpResponse, redirect
from apps.quiz.models import *
from apps.login.models import *

# Create your views here.
def quiz(request):
	if 'user_id' not in request.session:
		return redirect('/')
	context = {
		'categories' : Category.objects.all()
		}
	
	return render(request, 'quiz/quiz.html', context)

def create_quiz(request, id):
	if 'user_id' not in request.session:
		return redirect('/')
	
	context = {
		'questions' : Quiz.objects.make_quiz(id = id)
	}
	return render(request, 'quiz/take_quiz.html', context)

def quiz_end(request):
	pass