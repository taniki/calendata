import os

import calenda.parser.event

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
      event = calenda.parser.event.read(self.directory+"/"+event_file)

      if self.event_is_empty(event):
        self.count_empty = self.count_empty + 1

        self.empties.append(event_file)

    print("number of empty events: %i" % self.count_empty)

  def event_is_empty(self, event):
    return event is None

  def repair(self):

    print(self.empties)

    for event_id in self.empties:
      event = calenda.parser.event.parse(event_id)

    print(self.empties)
