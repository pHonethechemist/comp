from __future__ import unicode_literals

from django.db import models

class Content(models.Model):
  title = models.CharField(max_length = 500)
  subtitle = models.CharField(max_length = 500)
  contributors = models.ManyToManyField('Contributor', related_name = 'content')
  pub_date = models.DateTimeField('date published')

class Article(Content):
  pass

class Image(Content):
  pass

class Contributor(models.Model):
  pass

# I need to implement all of these models, but that is currently for another
# day. That seems like a lot of work at the moment. Check back in assignment3.md
# under Creating Models
