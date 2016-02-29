from datetime import date
from PIL import Image
import textwrap

class Content(object):
    # list to keep track of all pieces of content
    existing_content = []

    def __init__(self, year, month, day, contributors):
        # log each piece of content as existing upon creation
        self.existing_content.append(self)

        # TODO: Delete the following line and replace it with a line
        # that stores the year, month, and day (hint: check out datetime.date)
        self.creation_date = date(year, month, day)

        # list of contirbutors
        self.contributors = contributors

    # this defines a show method that has nothing in it, to be overridden later
    def show(self):
        print 'Implement this, bastard'

    # Since I want my subclasses to display contributors in the same way, it's a
    # good idea for them to use this method to get the contributors string from
    # their data.
    def format_contribs(self):
      contribs = ""
      if len(self.contributors) == 1:
        contribs += 'Contributor: '
      else:
        contribs += 'Contributors: '
      for c in self.contributors:
        contribs += (c + ', ')
      return contribs[:-2]


class Article(Content):
  def __init__(self, year, month, day, headline, content, contributors):
    super(Article, self).__init__(year, month, day, contributors)
    self.headline = headline
    self.content = content

  def show(self): 
    print '\n'
    print 'The Harvard Crimson\n'
    print self.creation_date.strftime('%A %d %B %Y\n')
    print self.headline
    print '{0}\n'.format(super(Article, self).format_contribs())
    print textwrap.fill(self.content, 80)
    print '\n'

class Picture(Content):
  def __init__(self, year, month, day, title, caption, path, contributors):
    super(Picture, self).__init__(year, month, day, contributors)
    self.title = title
    self.caption = caption
    self.path = path

  def show(self):
    print '\n'
    print 'The Harvard Crimson\n'
    print self.creation_date.strftime('%A %d %B %Y\n')
    print '{0}\n{1}\n\n{2}\n'.format(self.title, 
      super(Picture, self).format_contribs(), textwrap.fill(self.caption, 80))
    Image.open(self.path).show()
