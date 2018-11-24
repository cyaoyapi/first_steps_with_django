import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    """
    Model representing a servey question.
    """

    question_text = models.CharField("Question text", max_length=255)
    pub_date = models.DateTimeField("Date plublished")

    def __str__(self):
    	"""
    	Special method for best representation of objects.
    	"""

    	return f"{self.question_text}" # using f-string (python3.7)

    def was_published_recently(self):
    	"""
    	Return True if the question was published recently else False.
    	"""

    	return timezone.now() - datetime.timedelta(days=1) <= self.pub_date <= timezone.now()
    # Some settings to use was_published_recently as a field in administration site
    was_published_recently.admin_order_field = 'pub_date' 
    was_published_recently.boolean = True 
    was_published_recently.short_description = 'published recently ?' 

class Choice(models.Model):
	"""
	Model representing a choice of answer to a survey question.
	"""

	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField("Choice text", max_length=255)
	votes = models.IntegerField("Votes", default=0)

	def __str__(self):
		"""
    	Special method for best representation of objects.
		"""

		return f"{self.choice_text}"

