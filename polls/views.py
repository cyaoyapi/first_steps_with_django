from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Question, Choice

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

	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question':question})


def vote(request, question_id):
	"""
	Process a voting action : when the user clic on submit.
	"""

	question = get_object_or_404(Question, pk=question_id)
	try:
		choice_selected = Choice.objects.get(pk=request.POST['choice'])
	except (keyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html',{
			'question':question,
			'error_message':"You didn't select a choice",
		})
	else:
		choice_selected.votes += 1
		choice_selected.save()
		return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))

def results(request, question_id):
	"""
	Display a question and the results of votes
	"""

	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/results.html', {'question':question})
