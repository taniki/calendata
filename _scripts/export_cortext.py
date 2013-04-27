# -*- coding: utf-8 -*-

from calenda.corpus import Corpus
import calenda.exporter.cortext

dataset = "../_dataset"

corpus = Corpus(dataset)
calenda.exporter.cortext.generate(corpus, "all.csv")