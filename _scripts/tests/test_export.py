import os

from calenda.corpus import Corpus
import calenda.exporter.cortext

import csv

dataset_sample = "tests/dataset_sample"
test_destination = "cortext.csv"

def test_export_cortext_csv():
  corpus = Corpus(dataset_sample)

  calenda.exporter.cortext.generate(corpus, test_destination)

  rows = [ row for row in csv.reader(open(test_destination, "r"), delimiter="\t") ]

  os.remove(test_destination)

  # 11 files + 1 title row = 12 rows
  assert len(rows) == 12