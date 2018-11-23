from django.contrib import admin

from .models import Question, Choice

class QuestionAdmin(admin.ModelAdmin):
	"""
	A model to customize the form of question in the administration site.
	"""

	fields = ['pub_date','question_text']

# Register your models here.

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
