from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.

def index(resquest):
	""" Homepage vto say welcome to visitor. """

	return HttpResponse("Hello, welcome to our django website.\nWe're going to do a polls application.")