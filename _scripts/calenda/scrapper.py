# -*- coding: utf-8 -*-

import sys

import codecs

import urllib2
import yaml

from pyquery import PyQuery as pq
# import BeautifulSoup

# event : 207274

url = "http://calenda.org/search?q=*:*&primary=fdate&sort=datemisenligne_date&order=desc"