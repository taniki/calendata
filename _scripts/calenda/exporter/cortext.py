import os
import csv

import codecs

import calenda.parser.event

def generate(source, destination):
  print csv

  export = csv.writer(open(destination, "w"), delimiter = "\t" )

  export.writerow(['title' , 'categories'])

  for event_file in os.listdir(source):
    event = calenda.parser.event.read(source+"/"+event_file)

    if event is not None:
      line = [ event["metadata"]["title"], "***".join(event["metadata"]["categories"]) ]
      line = [ cell.encode("utf8")  for cell in line ]

      print line

      export.writerow(line)