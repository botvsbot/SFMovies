SFMovies
========

Problem Description: Search for movies filmed in San Francisco and display them on a map. The data is publicly available at <a href=https://data.sfgov.org/Culture-and-Recreation/Film-Locations-in-San-Francisco/yitu-d5am?>Film Locations</a>.

Focussed on Full Stack - Primarily used Python Django for the backend and Javascript and Twitter Bootstrap CSS files for the front-end.

The app is deployed at the following link: http://salty-dawn-5939.herokuapp.com/movies/


**Technical specs:**

* Backend - Python Django
* Database - sqlite3 for development and testing; Postgresql for deployment
* Frontend - Javascript, HTML and Twitter Bootstrap front-end framework
* Production/Deployment - AWS for the database and heroku for deployment


**Features:**

* Autocomplete search box for movies
* Partial search on movie names list all movie names and also drops a market in the map for all movies that match the search
* Tooltip on all the map-markers (activated upon click), with information regarding the address and some trivia about the place(fun facts)


**Learning curve/Experience:**

* I have quite a strong background in Python. But havent worked completely on a full-blown app. Have a beginner level experience in Django and no exprerience with Javascript and HTML/CSS. Did not use Backbone.js for the front-end as I found pretty good documentation for Django-JS/HTML communication online and just went with that. Finally, used the Twitter bootstrap for CSS-ing and presenting a nice and clean UI. Also, this was my first time integrating heroku and AWS with Python Django.


**Known issues/Things to do:**

* Clean up unicode characters (tilde and ampersand)
* App currently populates lat/lng by querying google maps location api from client side. Need to modify it to query from server side.
* Enable automatic update of the AWS database by periodically scrapping the data from DataSF.
* The home page is http://salty-dawn-5939.herokuapp.com/movies and not the root link. Need to make modifications to the urls.py file to make sure the root link is redirected to home page.
