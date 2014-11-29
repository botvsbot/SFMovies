from django.db import models
# Create your models here.
class Movies(models.Model):
	movie_id = models.IntegerField(default=0)
	title = models.CharField(max_length = 128)
	release_year = models.IntegerField(default=0)
	location_id = models.CharField(max_length = 128)
	fun_facts = models.CharField(max_length = 512, default = '')
	producer = models.CharField(max_length = 128)
	director = models.CharField(max_length = 128)
	distributor = models.CharField(max_length = 128)
	actor1 = models.CharField(max_length = 128)
	actor2 = models.CharField(max_length = 128)
	actor3 = models.CharField(max_length = 128)
	lat = models.DecimalField(decimal_places = 40,max_digits = 50, default = 0.0)
	lng = models.DecimalField(decimal_places = 40,max_digits = 50, default = 0.0)

	def __unicode__(self):
		return (self.title)
