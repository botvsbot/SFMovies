from django.test import TestCase
from movies.models import Movies
from django.core.urlresolvers import reverse
# Create your tests here.

def add_movie(movie_id, title, location):
	m = Movies.objects.get_or_create(movie_id=movie_id)[0]
	m.title = title
	m.location_id = location_id
	m.save()
	return m

class IndexViewTests(TestCase):

    def test_data_view_with_no_movies(self):
        """
        If no movies exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('data'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no movies present.")
        self.assertQuerysetEqual(response.context['movies'], [])

	def test_data_view_with_movies(self):

        """
                Ensure context_dictionary has the correct set of titles
        """

		add_movie(-1,"tmp","20")
		add_movie(-2,"test","40")
		add_movie(-3,"temp","60")
		add_movie(-4,"tmp test","San Francisco")

		response = self.client.get(reverse('data'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "tmp test temp")

		num_movies =len(response.context['movies'])
		self.assertEqual(num_movies , 4)

class MovieMethodTests(TestCase):

    def test_ensure_title_is_non_empty(self):

        """
                ensure_title_is_non_empty will be True for movies where title is a non-empty string
        """
        mov = Movies(movie_id=0,title='via')
        mov.save()
        self.assertEqual((len(mov.title) > 0), True)
