SFMovies
========

Problem Description: Search for movies filmed in San Francisco and display them on a map. The data is publicly available at <a href=https://data.sfgov.org/Culture-and-Recreation/Film-Locations-in-San-Francisco/yitu-d5am?>Film Locations</a>.

Focussed on Full Stack - Primarily used Python Django for the backend and Javascript and Twitter Bootstrap CSS files for the front-end.

The app is deployed at the following link: http://salty-dawn-5939.herokuapp.com/movies/


Technical specs:

Backend - Python Django

Database - sqlite3 for development and testing; Postgresql for deployment

Frontend - Javascript, HTML and Twitter Bootstrap front-end framework

Production/Deployment - AWS for the database and heroku for deployment


Features:

Autocomplete search box for movies

Tooltip on all the map-markers (activated upon click), with information regarding the address and some trivia about the place


Learning curve:

Strong background in Python; Beginner in Django and Javascript.


Known issues/Things to do:

Clean up unicode characters ()

App currently populates lat/lng by querying google maps location api from client side. Need to modify it to query from server side.

Enable automatic update of the AWS database by periodically scrapping the data from DataSF.
