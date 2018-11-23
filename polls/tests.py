import datetime

from django.test import TestCase
from django.utils import timezone

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

