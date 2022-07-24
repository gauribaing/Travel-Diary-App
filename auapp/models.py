from django.db import models

class TripModel(models.Model):
	srno = models.BigAutoField(primary_key=True)
	Destination = models.CharField(max_length=30)
	Date = models.DateField(verbose_name="Date (mm-dd-yyyy)")
	Text = models.TextField()
	Pic = models.FileField()
