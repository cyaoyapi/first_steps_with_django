import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question

# Create your tests here.

class QuestionModelTests(TestCase):
	"""
	All tests on Model 'Question'
	"""

	def test_was_published_recently_with_future_question(self):
		"""
		Unit Test
		---------
		Given : question with a future published date (variable pub_date > current date)
		When : call the methode 'was_published_recently'
		Then : return False
		"""

		future_question = Question(pub_date=timezone.now() + datetime.timedelta(days=30))
		self.assertIs(future_question.was_published_recently(), False)

	def test_was_published_recently_with_old_question(self):
		"""
		Unit Test
		---------
		Given : question with a old published date (variable pub_date < current date - 1 day)
		When : call the methode 'was_published_recently'
		Then : return False
		"""

		old_question = Question(pub_date=timezone.now() - datetime.timedelta(days=1, seconds=1))
		self.assertIs(old_question.was_published_recently(), False)

	def test_was_published_recently_with_recent_question(self):
		"""
		Unit Test
		---------
		Given : question with a recent published date (variable current date - 1 day <= pub_date <= current date)
		When : call the methode 'was_published_recently'
		Then : return False
		"""

		recent_question = Question(pub_date=timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59))
		self.assertIs(recent_question.was_published_recently(), True)

def create_question(question_text, days):
	"""
	Useful function for tests.
	It create and return a question with given 'question_text' and number of days.
	the number of days is positive for the future question and negative of old question.
	"""

	return Question.objects.create(question_text=question_text, pub_date=timezone.now() + 
		datetime.timedelta(days=days))


class QuestionIndexViewTests(TestCase):
	"""
	All tests on the view 'IndexView'.
	"""

	def test_no_questions(self):
		"""
		Unit Test
		---------
		Given : No questions existing in the database
		When : The user requests 'polls/index.html'
		Then : 
			- return a response with status_code = 200
			- display the message 'No polls are available.'
			- the context variable latest_questions_list = []
		"""

		# No question creation calling function 'create_question'
		response = self.client.get(reverse('polls:index'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "No polls are available.")
		self.assertQuerysetEqual(response.context['latest_questions_list'], [])

	def test_past_question(self):
		"""
		Unit Test
		---------
		Given : One question created with past date in the database
		When : The user requests 'polls/index.html'
		Then : The context variable 'latest_questions_list' must contains 
			the past question created.		
		"""

		create_question('Past Question ?', days=-30) # Past question created
		response = self.client.get(reverse('polls:index'))
		self.assertQuerysetEqual(response.context['latest_questions_list'], ['<Question: Past Question ?>'])

	def test_future_question(self):
		"""
		Unit Test
		---------
		Given : One question created with future date in the database
		When : The user requests 'polls/index.html'
		Then : 
			- display the message 'No polls are available.'
			- the context variable latest_questions_list = []		
		"""

		create_question('Future Question ?', days=30) # Future question created
		response = self.client.get(reverse('polls:index'))
		self.assertQuerysetEqual(response.context['latest_questions_list'], [])

	def test_future_and_past_questions(self):
		"""
		Unit Test
		---------
		Given : Deux questions created in the database
			- One with future date 
			- And one with past date 
		When : The user requests 'polls/index.html'
		Then : The context variable 'latest_questions_list' must contains 
			only the past question created and no the future question.			
		"""

		create_question('Future Question ?', days=30) # Future question created
		create_question('Past Question ?', days=-30) # Past question created
		response = self.client.get(reverse('polls:index'))
		self.assertQuerysetEqual(response.context['latest_questions_list'], ['<Question: Past Question ?>'])


	def test_two_past_questions(self):
		"""
		Unit Test
		---------
		Given : Two past questions created in the database
		When : The user requests 'polls/index.html'
		Then : The context variable 'latest_questions_list' must contains 
			the two past questions created.			
		"""

		create_question('Past Question 1 ?', days=-30) # Past question 1 created
		create_question('Past Question 2 ?', days=-5) # Past question 2 created
		response = self.client.get(reverse('polls:index'))
		self.assertQuerysetEqual(response.context['latest_questions_list'], ['<Question: Past Question 2 ?>', '<Question: Past Question 1 ?>'])

class QuestionDetailViewTests(TestCase):
	"""
	All tests on the view 'DetailView'.
	"""

	def test_future_question(self):
		"""
		Unit Test
		---------
		Given : One question created with future date in the database
		When : The user requests 'polls/detail.html'
		Then : Return Http404 page.		
		"""

		future_question = create_question('Future Question ?', days=30) # Future question created
		response = self.client.get(reverse('polls:detail', args=(future_question.id,)))
		self.assertEqual(response.status_code, 404)

	def test_past_question(self):
		"""
		Unit Test
		---------
		Given : One question created with past date in the database
		When : The user requests 'polls/detail.html'
		Then : The context variable 'question' must contains 
			the past question created.		
		"""

		past_question = create_question('Past Question ?', days=-30) # Past question created
		response = self.client.get(reverse('polls:detail', args=(past_question.id,)))
		self.assertContains(response, past_question.question_text)


class QuestionResultsViewTests(TestCase):
	"""
	All tests on the view 'ResultsView'.
	"""

	def test_future_question(self):
		"""
		Unit Test
		---------
		Given : One question created with future date in the database
		When : The user requests 'polls/results.html'
		Then : Return Http404 page.		
		"""

		future_question = create_question('Future Question ?', days=30) # Future question created
		response = self.client.get(reverse('polls:results', args=(future_question.id,)))
		self.assertEqual(response.status_code, 404)

	def test_past_question(self):
		"""
		Unit Test
		---------
		Given : One question created with past date in the database
		When : The user requests 'polls/results.html'
		Then : The context variable 'question' must contains 
			the past question created.		
		"""

		past_question = create_question('Past Question ?', days=-30) # Past question created
		response = self.client.get(reverse('polls:results', args=(past_question.id,)))
		self.assertContains(response, past_question.question_text)