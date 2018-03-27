from django.db import models
from apps.login.models import User
from random import choice
import csv, random

class Quiz_Manager(models.Manager):
	def make_quiz(self, id):
		quiz = {}
		answer_list = []
		people_list = []
		people_dict = {'people' : People.objects.filter(category = Category.objects.get(id = id))}
		for person in people_dict['people']:
			people_list.append({'athlete': person})
		random.shuffle(people_list)
		answer = people_list.pop()
		trivia = answer['athlete'].abstract
		answer_list.append({'answer': answer,'value': True})
		for k in range(0,3):
			answer = people_list.pop()
			answer_list.append({'answer': answer,'value': False,})
		random.shuffle(answer_list)
		quiz['trivia'] = trivia
		quiz['answer_list'] = answer_list
		return quiz #and magic

class Category (models.Model):
	activity_type = models.CharField(max_length=255)
	# objects = Catagory_Manager()

class Quiz(models.Model):
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
	objects = Quiz_Manager()

class People(models.Model):
	name = models.CharField(max_length=255)
	abstract = models.TextField(default = "")
	category = models.ForeignKey(
		Category, 
		on_delete=models.CASCADE, 
		related_name  = "category"
	)

	def __repr__(self):
		return f'<Quiz object: {self.name}'






#