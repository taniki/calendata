# -*- coding: utf-8 -*-
import sys

import codecs

import urllib2
import yaml

from pyquery import PyQuery as pq
# import BeautifulSoup

target_dir = '../_dataset'

metadata_order = [ ("title", "permalink"), ("type", "subject", "categories") ]

def parse(event_id):
  f = codecs.open("%s/%s.md" % (target_dir, event_id), "w", "utf-8")

  print "parsing: %s" % ("http://calenda.org/%s" % event_id)

  metadata = {}
  metadata['permalink'] = "http://calenda.org/%s" % event_id

  page = pq(url = metadata['permalink'])

#  print(page)

  metadata['title'] = "%s" % page('#main h1 a').html()

  kw = page('#motscles ul li').html()

  metadata['keywords'] = kw.split(', ') if kw else []
  metadata['dates'] = [ pq(d).html() for d in page('#dates ul li') ]

  metadata['type'] = page('#icon > a').html()
  metadata['subject'] = page('#icon > span').html()
#    metadata['subject_id'] = page('#icon > span').html().strip()

  metadata['categories'] = [ pq(d).html() for d in page('#listcategories ul li a') ]

#  print(metadata)

  f.write('---\n')
  yaml.safe_dump({ k : v for k,v in metadata.items() if k in metadata_order[0] }, f, default_flow_style=False, encoding=('utf-8'), allow_unicode=True)

  f.write('\n')

  yaml.safe_dump({ k : v for k,v in metadata.items() if k in metadata_order[1] }, f, default_flow_style=False, encoding=('utf-8'), allow_unicode=True)

  f.write('\n')

  yaml.safe_dump({ k : v for k,v in metadata.items() if (k not in metadata_order[1]) and (k not in metadata_order[0]) }, f, default_flow_style=False, encoding=('utf-8'), allow_unicode=True)

  f.write('---\n')

  if(page('#resume > div').html() is not None):
#    print( page('#resume > div').html().strip() )
    f.write( page('#resume > div').html().strip() )

  f.write('\n---\n')

  if(page('#annonce > div').html() is not None):
#    print( "\n".join([ l.strip() for l in page('#annonce > div').html().split('\n') ])  )
    f.write( "\n".join([ l.strip() for l in page('#annonce > div').html().split('\n') ]) )

 

def read(fh):
  f = codecs.open(fh, "r", "utf-8")

  front_matter = f.read().split("---")

  if len(front_matter) > 3:
    return {
      'metadata' : yaml.load(front_matter[1]),
      'abstract' : front_matter[2],
      'content' : front_matter[3]
    }
  else:
    return None

class Event:
  def __init__(self, id):
    self.id = id
    self.permalink = "http://calenda.org/%s" % id
    self.title = None

    self.type = None

    self.subject = None
    self.keywords = []
    self.categories = []

    self.dates = []

    self.abstract = None
    self.content = None

  def set_dataset(self, dataset_dir):
    self.dataset = dataset_dir

  def scrap(self):
    self.html = pq(url = self.permalink)

  def parse(self):
    if(self.html('#main h1 a').html()):
      self.title = "%s" % self.html('#main h1 a').html()

    kw = self.html('#motscles ul li').html()
    self.keywords = kw.split(', ') if kw else []

    self.dates = [ pq(d).html() for d in self.html('#dates ul li') ]

    self.type = self.html('#icon > a').html()
    self.subject = self.html('#icon > span').html()

    self.categories = [ pq(d).html() for d in self.html('#listcategories ul li a') ]

    self.abstract = self.html('#resume > div').html()
    if(self.abstract is not None):
      self.abstract = self.abstract.strip()

    self.content = self.html('#annonce > div').html()
    if(self.content is not None):
      self.content = "\n".join([ l.strip() for l in self.content.split('\n') ])

  def open(self):
    path = "%s/%s.md" % (self.dataset, self.id)

    f = codecs.open(path, "r", "utf-8")

    front_matter = f.read().split("---")
    
    self.metadata = yaml.load(front_matter[1])
    
    self.title = self.metadata["title"]
    self.permalink = self.metadata["permalink"]

    self.abstract = front_matter[2]
    self.content = front_matter[3]