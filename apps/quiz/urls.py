from django.urls import include, path
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.quiz, name = 'quiz_home'),
    path('<int:id>', views.create_quiz, name = 'create_quiz'),
    path('end', views.quiz_end, name = 'quiz_end'),
    ]