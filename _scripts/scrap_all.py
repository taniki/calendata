# -*- coding: utf-8 -*-

from calenda.search import Search
from calenda.corpus import Corpus
from calenda.event import Event

url = "http://calenda.org/search?q=*:*&primary=fdate&sort=datemisenligne_date&order=desc"
dataset = "../_dataset"

corpus = Corpus(dataset)
search = Search(url)

search.scrap()
search.parse()

while len(search.current_results) > 0 :
  for event_id in search.current_results:
    event = corpus.read(event_id)

    if event.is_stored is False :
      print "[grabbing] %s" % event_id

      event = Event(event_id)
      event.scrap()
      event.parse()

      corpus.store(event)
    
    else:
      print "[skipping] %s (already in corpus)" % event_id

  search.walk()
  search.scrap()
  search.parse()