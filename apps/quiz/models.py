from django.db import models
from apps.login.models import User
from random import *
import csv
# Create your models here.


#************Quiz Table*************
class QuizScoreManager(models.Manager):
	def make_quiz(self, postData):
		quiz = []
		question = {
			'trivia' : "No Abstract Found",
			'answerA' : ["No Name", False],
			'answerB' : ["No Name", False],
			'answerC' : ["No Name", False],
			'answerD' : ["No Name", False]
		}
		#Generate 10 Questions
		for k in range(0,10):
			#List of all people within the category that the client selects
			people_list = People.objects.filter(category = Catagory.objects.get(id = postData['category_id']))
			#For Loop suffles the list of people that fit the catagory into a random order
			for i in range (0,len(people_list)):
				temp = people_list[i]
				random_index = randint(0, len(people_list))-1
				temp2 = people_list[random_index]
				people_list[random_index] = temp
				people_list[i] = temp2
			#Pull Four people from the list of all people that fit the client's category. The first person pull will be our question
			randomPersonA = people_list.pop()
			randomPersonB = people_list.pop()
			randomPersonC = people_list.pop()
			randomPersonD = people_list.pop()
			#Set the questions trivia to the first random person's abstract
			question['trivia'] = randomPersonA.abstract
			answerList = ['answerA','answerB','answerC','answerD']
			#Set the value of the random Person's name to a random answer key for the question
			question[answerList.pop(randint(0,len(answerList))-1)] = [randomPersonA.name, True]
			question[answerList.pop(randint(0,len(answerList))-1)] = [randomPersonB.name, False]
			question[answerList.pop(randint(0,len(answerList))-1)] = [randomPersonC.name, False]
			question[answerList.pop(randint(0,len(answerList))-1)] = [randomPersonD.name, False]
			#Add the question to the quiz
			quiz.append(question)
		#Return the the list of all questions
		return quiz

class QuizScore (models.Model):
	score = models.IntegerField()
	user = models.ForeignKey(User, related_name = "testie")
	catagory = models.ForeignKey(Category, related_name  = "quiz")
	objects = QuizScoreManager()
#***********END Quiz Table *********

#************Category Table*************
class Category (models.Model):
	activity_type = models.CharField(max_length=255)
	#objects = CatagoryManager()
#***********END Category Table *********

class QuizScore(models.Model):
	score = models.IntegerField()
	user = models.ForeignKey(
		User, 
		on_delete=models.CASCADE, 
		related_name = "testie"
	)
	
	category = models.ForeignKey(
		Category, 
		on_delete=models.CASCADE, 
		related_name  = "quiz_type"
	)
	# objects = QuizScoreManager()
#***********END Quiz Table *********

#************Athlete Table*************
class People(models.Model):
	name = models.CharField(max_length=255)
	abstract = models.TextField(default = "")
	category = models.ForeignKey(
		Category, 
		on_delete=models.CASCADE, 
		related_name  = "category"
	)
	#objects = PeopleManager()
#***********END Athlete Table *********
