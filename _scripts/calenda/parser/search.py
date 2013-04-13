import sys
import codecs
import urllib2

from pyquery import PyQuery as pq

import calenda.parser.event

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