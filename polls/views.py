from django.http import HttpResponse, Http404
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

	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404(f"This question does not exist")
	return render(request, 'polls/detail.html', {question:question})

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