import string, collections

def swapchars(str):
  common = collections.Counter(str.lower().translate(None, string.punctuation
             + ' ')).most_common()
  return str.replace(common[0][0], common[-1][0])

# print swapchars("I really like to fuck with shit aaaaaaaaaaaaaaaaaaaaaaa")

def sortcat(i, *args):
  ordered = sorted(args, key = len)
  ordered.reverse()
  length = len(ordered)
  ret = ""
  if i == -1 or i > length:
    for x in xrange(length):
      ret += ordered[x]
  else:
    for x in xrange(i):
      ret += ordered[x]
  return ret


# print sortcat(-1, 'shit', 'kj', 'w', 'kjkjkjkjkjkjkjkjkj')
# sortcat(2, 'shit', 'fuck', 'stack')

abbrev = {}

def create_abbrev():
  read = open('states.txt', 'r')
  for line in read:
    parts = line.replace('\n', '').split(',')
    abbrev[parts[1]] = parts[0]

create_abbrev()

def find_abbrev(ab):
  return states[ab.upper()]

# print find_abbrev("NC")

def rev_find_abbrev(name):
  for ab, full in abbrev.iteritems():
    if full.lower() == name.lower():
      return ab

print rev_find_abbrev('alabama')
