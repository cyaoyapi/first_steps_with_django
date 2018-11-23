from django.http import HttpResponse
from django.shortcuts import render

from .models import Question

# Create your views here.

def index(request):
	""" 
	List the recents questions. 
	"""

	lastest_questions_list = Question.objects.order_by('-pub_date')[:5]
	
	context = {
		'lastest_questions_list':lastest_questions_list
	}
	return render(request, 'polls/index.html', context)

def detail(request, question_id):
	"""
	Display a question and its different choices for voting. 
	"""

	return HttpResponse(f"You're looking at question {question_id}")

def results(request, question_id):
	"""
	Display a question and the results of votes
	"""

	return HttpResponse(f"You're looking at the results of question {question_id}")

def vote(resquest, question_id):
	"""
	Process a voting action : when the user clic on submit.
	"""

	return HttpResponse(f"You're voting at the question {question_id}")