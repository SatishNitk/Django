from django.db import models

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length=290)
	image = models.ImageField(upload_to='images/')
	pub_date = models.DateTimeField()
	body = models.TextField()

	def summary_of_blog(self):
		return self.body[:50]
	def pub_date_formated(self):
		return self.pub_date.strftime("%b %e, %Y")
	def __str__(self):
		return self.title


