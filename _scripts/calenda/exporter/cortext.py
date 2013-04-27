import os
import csv

import codecs

from calenda.corpus import Corpus

metadata = ['title' , "subject", 'categories', "keywords", 'publisher']

def generate(corpus, destination):
  export = csv.writer(open(destination, "w"), delimiter = "\t" )

  export.writerow(metadata)

  for event_file in corpus.listdir:

    print event_file

    (event_id, format) = event_file.split(".")

    event = corpus.read(event_id)

    for m in metadata:
      if event.__dict__[m] is None:
        event.__dict__[m] = ""
      elif isinstance(event.__dict__[m], (list, tuple)):
        event.__dict__[m] = "***".join(event.__dict__[m])

      event.__dict__[m] = event.__dict__[m].encode("utf8")

    line = [ event.__dict__[m] for m in metadata ]

    print line

    export.writerow(line)