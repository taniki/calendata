import sys
import codecs
import urllib2

from pyquery import PyQuery as pq

from calenda.event import Event

def parse(url):
  "prelimenary parsing"

  print url

  content = pq(url = url)

  count = 0

  results = content('#results .list_entry')

  while len(results) > 0:
    parse_results(results)

    temp = int(count) + 20

    count += len(results)

    # print temp

    content = pq(url = url+'&start=%i' % temp)
    results = content('#results .list_entry')

  print count

def parse_results(results):
  for result in results:
    entry = pq(result);

    a = entry('.title a').attr('href');
    title = entry('.title a').html()

    # print a
    print "%s: %s" % (a, title)
    calenda.parser.event.parse(a)


class Search:
  def __init__(self, entrypoint):
    self.entrypoint = entrypoint

    self.pager_current = entrypoint
    self.pager_next = None

    self.current_html = None
    self.current_results = []

    self.count = 0
    self.expected = 0

  def scrap(self):
    """scrap a search page and set the pager to next page"""

    self.current_html = pq(url = self.pager_current)

    self.pager_next = self.pager_current+'&start=%i' % (int(self.count) + 20)

  def parse(self):
    """extract list of events from a search page"""

    self.current_results = self.current_html("#results .list_entry")
    self.count += len(self.current_results)

  def walk(self):
    """switch to next page"""

    self.pager_current = self.pager_next
    self.pager_next = None