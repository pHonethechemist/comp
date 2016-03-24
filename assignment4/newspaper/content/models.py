from __future__ import unicode_literals

from django.db import models
import textwrap

class Content(models.Model):
  title = models.CharField(max_length = 500)
  subtitle = models.CharField(max_length = 500)
  contributors = models.ManyToManyField('Contributor', related_name = 'content')
  pub_date = models.DateTimeField('date published')

  def format_contribs(self):
    contribs = ""
    l = len(self.contributors.all())
    if l == 1:
      contribs += 'Contributor: '
    else:
      contribs += 'Contributors: '
    for c in self.contributors.all():
      contribs += (c.__unicode__() + ', ')
    return contribs[:-2]

class Article(Content):
  text = models.TextField(default = 'put yo article right up in here')

  def show(self):
    return self.pub_date.strftime('%A %d %B %Y\n') + self.title + '\n\n' + \
    '{0}\n'.format(super(Article, self).format_contribs()) + \
    textwrap.fill(self.text, 80) + '\n'

  def __unicode__(self):
    return self.title

class Image(Content):
  path = models.CharField(default = 'path', max_length = 500)

  def __unicode__(self):
    return self.path

class Contributor(models.Model):
  first_name = models.CharField(default='first name', max_length = 50) 
  last_name = models.CharField(default='last name', max_length = 50)
 
  def die(self):
    self.delete()

  def __unicode__(self):
    return (self.first_name + ' ' + self.last_name)

