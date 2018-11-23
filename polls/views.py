from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import loader

from .models import Question

# Create your views here.

def index(resquest):
	""" 
	List the recents questions. 
	"""

	lastest_questions_list = Question.objects.order_by('-pub_date')[:5]
	template = loader.get_template('polls/index.html')
	context = {
		'lastest_questions_list':lastest_questions_list
	}
	return HttpResponse(template.render(context, resquest))

def detail(resquest, question_id):
	"""
	Display a question and its different choices for voting. 
	"""

	return HttpResponse(f"You're looking at question {question_id}")

def results(resquest, question_id):
	"""
	Display a question and the results of votes
	"""

	return HttpResponse(f"You're looking at the results of question {question_id}")

def vote(resquest, question_id):
	"""
	Process a voting action : when the user clic on submit.
	"""

	return HttpResponse(f"You're voting at the question {question_id}")