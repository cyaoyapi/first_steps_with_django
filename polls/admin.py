from django.contrib import admin

from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
	"""
	Using it to add Choice form as sub-form of Question form in administration site.
	"""

	model = Choice
	extra = 3
	


class QuestionAdmin(admin.ModelAdmin):
	"""
	A model to customize the form of question in the administration site.
	"""
	list_display = ('question_text', 'pub_date', 'was_published_recently')
	fieldsets = [
		(None , {'fields': ['question_text']}),
		('Date information' , {'fields': ['pub_date']}),
	]
	inlines = [ChoiceInline]

# Register your models here.

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)