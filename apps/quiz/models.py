from django.db import models

from random import *
# Create your models here.


#************Quiz Table*************
class QuizScoreManager(models.Manager):
	def make_quiz(self, postData):
		quiz = []
		question {}

		people_list = People.objects.filter(category = Catagory.objects.get(id = postData['category_id']))
		#For Loop suffles the list of people that fit the catagory into a random order
		for i in range (0,len(people_list)):
			temp = people_list[i]
			random_index = randint(0, len(people_list))-1
			temp2 = people_list[random_index]
			people_list[random_index] = temp
			people_list[i] = temp2
		#loop pulls the first 10 people from the randomly order list of people into the quiz
		for i in range (0,10):
			popped = people_list.pop(i)
			question['trivia'] = popped.abstract
			question['answer'] = popped.name
			quiz.append(question)
		return quiz


class QuizScore (models.Model):
	score = models.IntegerField()
	user = models.ForeignKey(User, related_name = "testie")
	catagory = models.ForeignKey(Category, related_name  = "category")
	objects = QuizScoreManager()
#***********END Quiz Table *********

#************Category Table*************
class Category (models.Model):
	activity_type = models.CharField(max_length=255)
	#objects = CatagoryManager()
#***********END Category Table *********

#************Athlete Table*************
class People(models.Model):
	name = models.CharField(max_length=255)
	abstract = models.TextField(default = "")
	category = models.ForeignKey(Category, related_name  = "category")
	#objects = PeopleManager()
#***********END Athlete Table *********