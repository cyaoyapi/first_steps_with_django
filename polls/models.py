from django.db import models

# Create your models here.

class Question(models.Model):
    """
    Model representing a servey question.
    """

    question_text = models.CharField("Question text", max_length=255)
    pub_date = models.DateTimeField("Date plublished")


class Choice(models.Model):
	"""
	Model representing a choice of answer to a survey question
	"""

	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField("Choice text", max_length=255)
	votes = models.IntegerField("Votes", default=0)
		
