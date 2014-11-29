from movies.models import Movies
import sys
def run_search(query):
	results = []
	unique_titles = []
	movie_list = Movies.objects.all()
	for movie in movie_list:
		if query.lower() in str(movie).lower():
			#print >>sys.stderr, movie, type(movie.title), movie.lat, movie.lng
			results.append(movie)
			unique_titles.append(movie.title)
	unique_titles = sorted(list(set(unique_titles)))
	return [results, unique_titles]
