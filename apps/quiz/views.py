from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def quiz(request):
	if 'user_id' not in request.session:
		return redirect('/')

	return render(request, 'quiz/quiz.html')