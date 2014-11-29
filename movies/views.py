#from django.template import render
from django.shortcuts import render
from movies.models import Movies
import json
import random
import datetime
import time
import sys
from django.db import connection
from django import forms
from django.shortcuts import render_to_response
from movies.search import run_search
from movies.filter_movies import unique_movie_list

# Create your views here.
from django.http import HttpResponse

def index(request):
	return render(request, 'movies/index.html')

def da(request):
	result_list = []
	unique_titles = []
	movie_list = unique_movie_list()
	#print >> sys.stderr, movie_list
	if request.method == 'POST':
		query = request.POST['query'].strip()
		#print >>sys.stderr, query
		if query:
			# Run our search function to get the results list!
			[result_list, unique_titles] = run_search(query)
			print >>sys.stderr, result_list
	context_dict = {'result_list':result_list, 'movie_list':movie_list, 'unique_titles':unique_titles}	
	return render(request, 'movies/da.html', context_dict)

def about(request):
	return render(request, 'movies/about.html')

def data(request):
	movie_list = unique_movie_list()
	#print >>sys.stderr, movie_list
	context_dict = {'movies': movie_list}
	#print >>sys.stderr, context_dict
	# Render the response and send it back!
	return render(request, 'movies/data.html', context_dict)
