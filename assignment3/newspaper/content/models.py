from __future__ import unicode_literals

from django.db import models

class Content(models.Model):
  title = models.CharField(max_length = 500)
  subtitle = models.CharField(max_length = 500)
  contributors = models.ManyToManyField('Contributor', related_name = 'content')
  pub_date = models.DateTimeField('date published')
'''
  def format_contribs():
    contribs = ""
    if len(contributors) == 1:
      contribs += 'Contributor: '
    else:
      contribs += 'Contributors: '
    for c in contributors:
      contribs += (c + ', ')
    return contribs[:-2]
'''

class Article(Content):
#use TextField for articles
  
  text = models.TextField(default = 'put yo article right up in here')
  '''
  def show(): 
    print '\n'
    print 'The Harvard Crimson\n'
    print pub_date.strftime('%A %d %B %Y\n')
    print title
    print '{0}\n'.format(super(Article, self).format_contribs())
    print textwrap.fill(text, 80)
    print '\n'
  '''

class Image(Content):
  path = models.CharField(default = 'path', max_length = 500)

class Contributor(models.Model):
  first_name = models.CharField(default='first name', max_length = 50) 
  last_name = models.CharField(default='last name', max_length = 50) 
  content = Content.objects.filter(contributors = objects.filter(first_name =
    first_name).filter(last_name = last_name))

  def die():
    objects.filter(first_name = first_name).filter(last_name =
        last_name).delete()


# I need to implement all of these models, but that is currently for another
# day. That seems like a lot of work at the moment. Check back in assignment3.md
# under Creating Models
