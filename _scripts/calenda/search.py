import sys
import codecs
import urllib2
import urlparse

from pyquery import PyQuery as pq

from calenda.event import Event

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

    pager = "&".join([ url_part for url_part in self.pager_current.split("&") if not url_part.startswith(("start=", )) ])

    self.pager_next = pager+'&start=%i' % (int(self.count) + 20)

  def parse(self):
    """extract list of events from a search page"""

    results = self.current_html("#results .list_entry")

    self.current_results = []

    for entry in results:
      e = pq(entry)

      event_id = e('.title a').attr('href')

      self.current_results.append(event_id)

    self.count += len(self.current_results)

  def walk(self):
    """switch to next page"""

    self.pager_current = self.pager_next
    self.pager_next = None