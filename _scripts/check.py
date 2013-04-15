from calenda.corpus import Corpus

corpus = Corpus("../_dataset")

corpus.check()
# corpus.empties = [ "187021" ]
## repair
corpus.repair()