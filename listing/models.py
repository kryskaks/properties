from django.db import models

class Property(models.Model):
	city = models.CharField(max_length=200)
	geo_lon = models.FloatField()
	bedrooms = models.IntegerField()
	zip_code = models.CharField(max_length=10)
	approx_sqft = models.FloatField(null=True)
	street_suffix = models.CharField(max_length=30)
	unit_number = models.CharField(null=True, max_length=10)
	bathrooms = models.IntegerField()
	street_number = models.IntegerField()
	street_name = models.CharField(max_length=100)
	geo_lat = models.FloatField()
	list_price = models.IntegerField()
	year_built = models.IntegerField()