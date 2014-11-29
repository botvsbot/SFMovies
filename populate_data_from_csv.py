import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SFMovies.settings')

import django
django.setup()
import csv

from movies.models import Movies

import urllib
import json

googleGeocodeUrl = 'http://maps.googleapis.com/maps/api/geocode/json?'

def get_coordinates(query, from_sensor=False):
    query = query + " San Francisco"
    try:
        query = query.encode('utf-8')
    except UnicodeDecodeError:
        return 0.0,0.0
    params = {
        'address': query,
        'sensor': "true" if from_sensor else "false"
    }
    url = googleGeocodeUrl + urllib.urlencode(params)
    json_response = urllib.urlopen(url)
    response = json.loads(json_response.read())
    if response['results']:
        location = response['results'][0]['geometry']['location']
        latitude, longitude = location['lat'], location['lng']
        #print query, latitude, longitude
    else:
        latitude, longitude = 0.0, 0.0
        #print query, "<no results>"
    return latitude, longitude

def populate():
	my_dict = {}
	count = 0
	f = csv.reader(open('Film_Locations_in_San_Francisco.csv', 'r'))
	for row in f:
		if count == 0:
			keys = row
			count += 1
		else:
			for k,v in zip(keys,row):
				my_dict[k] = v
			lat,lng = get_coordinates(my_dict["Locations"])
			add_data(count, my_dict["Title"], my_dict["Release Year"], my_dict["Locations"], my_dict["Production Company"], my_dict["Director"], my_dict["Distributor"], my_dict["Actor 1"], my_dict["Actor 2"], my_dict["Actor 3"], lat, lng)	
			count += 1

def add_data(movie_id, title, release_year, location_id, producer, director, distributor, actor1, actor2, actor3, lat, lng):
    p = Movies.objects.update_or_create(movie_id = movie_id, title = title, release_year = release_year, location_id = location_id, producer = producer, director = director, distributor = distributor, actor1 = actor1, actor2 = actor2, actor3 = actor3, lat = lat, lng = lng)[0]
    return p

# Start execution here!
if __name__ == '__main__':
	print "Starting food truck population script..."
	populate()
