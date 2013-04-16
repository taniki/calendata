import os
import csv

import codecs

from calenda.corpus import Corpus

def generate(corpus, destination):
  export = csv.writer(open(destination, "w"), delimiter = "\t" )

  export.writerow(['title' , 'categories'])

  for event_file in corpus.listdir:

    (event_id, format) = event_file.split(".")

    event = corpus.read(event_id)

    line = [ event.title, "***".join(event.categories) ]
    line = [ cell.encode("utf8")  for cell in line ]

    print line

    export.writerow(line)