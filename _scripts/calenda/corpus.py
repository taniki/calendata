import os
import codecs

import yaml

from calenda.event import Event

metadata_order = [
  ("title", "permalink"),
  ("publisher",),
  ("type", "subject", "categories"),
  ("keywords", "dates")
]

class Corpus:

  def __init__(self, dataset_dir):

    self.directory = dataset_dir

    self.count_empty = 0
    self.empties = []

    print("reading corpus directory")
    self.listdir = os.listdir(self.directory)

    self.total = len(self.listdir)
    print("number of events: %i" % self.total)

  def check(self):

    for event_file in self.listdir:
      event = Event(event_file)
      event.set_dataset(self.directory)

      if self.event_is_empty(event):
        self.count_empty = self.count_empty + 1

        self.empties.append(event_file)

    print("number of empty events: %i" % self.count_empty)

  def event_is_empty(self, event):
    return event.content is None

  def repair(self):

    print(self.empties)

    empties = []

    for empty in self.empties:
      event_id = empty.split(".")[0]
      empties.append(event_id)

    for event_id in empties:
      event = Event(event_id)
      event.scrap()
      event.parse()
      self.store(event)

      if( not self.event_is_empty(event)):
        self.empties.remove(event_id+".md")

  def read(self, event_id):
    event = Event(event_id)
    event.set_dataset(self.directory)
    event.open()

    return event

  def store(self, event):
    f = codecs.open("%s/%s.md" % (self.directory, event.id), "w", "utf-8")

    f.write('---\n')

    for i in range(len(metadata_order)):
      meta = {}

      for key in metadata_order[i]:
        meta[key] = event.__dict__[key]

      yaml.safe_dump(meta, f, default_flow_style=False, encoding=('utf-8'), allow_unicode=True)

      f.write('\n')

    f.write('---\n')

    if event.abstract is not None:
      f.write( event.abstract )

    f.write('\n---\n')

    if event.content is not None:
      f.write( event.content )