from movies.models import Movies
import sys
def unique_movie_list():
	results = []
	movie_list = Movies.objects.all()
	for movie in movie_list:
			#print >>sys.stderr, movie.title
			results.append(movie.title)
	results = sorted(list(set(results)))
	return results
