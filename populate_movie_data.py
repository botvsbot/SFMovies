import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SFMovies.settings')

import django
django.setup()

from movies.models import Movies

import urllib, urllib2
import json

googleGeocodeUrl = 'http://maps.googleapis.com/maps/api/geocode/json?'

def get_coordinates(query, from_sensor=False):
    if query is None:
        return 0.0, 0.0
    query = query + " San Francisco"
    try:
        query = query.encode('utf-8')
    except UnicodeDecodeError:
        return 0.0, 0.0
    params = {
        'address': query,
        'sensor': "true" if from_sensor else "false"
    }
    url = googleGeocodeUrl + urllib.urlencode(params)
    json_response = urllib.urlopen(url)
    response = json.loads(json_response.read())
    #print response
    if response['results']:
        location = response['results'][0]['geometry']['location']
        latitude, longitude = location['lat'], location['lng']
    else:
        latitude, longitude = 0.0, 0.0
    return latitude, longitude

def populate():
	my_dict = {}
	count = 0
	response = urllib2.urlopen("https://data.sfgov.org/api/views/yitu-d5am/rows.json")
	f = json.load(response)
		
	for row in f["data"]:
		count += 1
		for i in xrange(8,len(row)):
			if row[i] is None:
				row[i] = ''
		lat,lng = get_coordinates(row[10])
		add_data(count, row[8], row[9], row[10], row[11], row[12], row[14], row[13], row[16], row[17], row[18], lat, lng)
		#print row[8], count
		#if count ==5:
		#	break

def add_data(movie_id, title, release_year, location_id, fun_facts, producer, director, distributor, actor1, actor2, actor3, lat, lng):
    p = Movies.objects.update_or_create(movie_id = movie_id, title = title, release_year = release_year, location_id = location_id, fun_facts = fun_facts, producer = producer, director = director, distributor = distributor, actor1 = actor1, actor2 = actor2, actor3 = actor3, lat = lat, lng = lng)[0]
    return p

# Start execution here!
if __name__ == '__main__':
	print "Starting SFMovies population script..."
	populate()
