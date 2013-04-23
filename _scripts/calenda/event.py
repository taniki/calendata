# -*- coding: utf-8 -*-
import sys

import codecs

import urllib2
import yaml

from pyquery import PyQuery as pq

class Event:
  def __init__(self, id):
    self.id = id
    self.permalink = "http://calenda.org/%s" % id
    self.title = None
    self.publisher = None

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

    self.publisher = self.html('#pubdate').html()
    self.publisher = self.publisher.split("par")
    self.publisher = self.publisher[1].strip()

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

    self.is_stored = True

    try:
      f = codecs.open(path, "r", "utf-8")

      front_matter = f.read().split("---")
      
      if len(front_matter) > 3:
        self.metadata = yaml.load(front_matter[1])
        
        self.title = self.metadata["title"]
        self.permalink = self.metadata["permalink"]

        self.abstract = front_matter[2]
        self.content = front_matter[3]

      else:
        pass
    
    except IOError, e:
      self.is_stored = False