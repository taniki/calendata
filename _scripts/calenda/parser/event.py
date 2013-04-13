# -*- coding: utf-8 -*-
import sys

import codecs

import urllib2
import yaml

from pyquery import PyQuery as pq
# import BeautifulSoup

target_dir = '../_dataset_test'

metadata_order = [ ("title", "permalink"), ("type", "subject", "categories") ]

def parse(event_id):
  f = codecs.open("%s/%s.md" % (target_dir, event_id), "w", "utf-8")

  metadata = {}
  metadata['permalink'] = "http://calenda.org/%s" % event_id

  page = pq(url = metadata['permalink'])

  metadata['title'] = "%s" % page('#main h1 a').html()

  kw = page('#motscles ul li').html()

  metadata['keywords'] = kw.split(', ') if kw else []
  metadata['dates'] = [ pq(d).html() for d in page('#dates ul li') ]

  metadata['type'] = page('#icon > a').html()
  metadata['subject'] = page('#icon > span').html()
#    metadata['subject_id'] = page('#icon > span').html().strip()

  metadata['categories'] = [ pq(d).html() for d in page('#listcategories ul li a') ]

  f.write('---\n')
  yaml.safe_dump({ k : v for k,v in metadata.items() if k in metadata_order[0] }, f, default_flow_style=False, encoding=('utf-8'), allow_unicode=True)

  f.write('\n')

  yaml.safe_dump({ k : v for k,v in metadata.items() if k in metadata_order[1] }, f, default_flow_style=False, encoding=('utf-8'), allow_unicode=True)

  f.write('\n')

  yaml.safe_dump({ k : v for k,v in metadata.items() if (k not in metadata_order[1]) and (k not in metadata_order[0]) }, f, default_flow_style=False, encoding=('utf-8'), allow_unicode=True)

  f.write('---\n')

  if(page('#resume > div').html() is not None):
    f.write( page('#resume > div').html().strip() )

  f.write('\n---\n')

  if(page('#annonce > div').html() is not None):
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

