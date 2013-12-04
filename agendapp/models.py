from django.db import models

# Create your models here.

class Note(models.Model):
	nota = models.CharField(max_length=100)
	pub_date = models.DateTimeField('date published')

	def __unicode__(self):  # Python 3: def __str__(self):
		return self.nota
