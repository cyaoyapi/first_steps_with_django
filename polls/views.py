from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Question, Choice

# Create your views here.

class IndexView(generic.ListView):
	""" 
	List the recents questions. 
	"""

	template_name = 'polls/index.html'
	context_object_name = 'latest_questions_list'

	def get_queryset(self):
		return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	"""
	Display a question and its different choices for voting. 
	"""

	model = Question
	template_name = 'polls/detail.html'


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

class ResultsView(generic.DetailView):
	"""
	Display a question and the results of votes
	"""

	model = Question
	template_name = 'polls/results.html'
