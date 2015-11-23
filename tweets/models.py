from django.db import models

# Create your models here.
class NewsChannel(models.Model):
	newsChannelName = models.CharField(max_length=50)
	
	def __unicode__(self):
		return self.newsChannelName