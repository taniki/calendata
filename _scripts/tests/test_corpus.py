from calenda.corpus import Corpus

dataset_dir = "tests/dataset_sample"
dataset_with_errors_dir = "tests/dataset_error"

def test_list():
  corpus = Corpus(dataset_dir)

  assert len(corpus.listdir) > 0

def test_detect_empties():
  corpus = Corpus(dataset_with_errors_dir)

  corpus.check()

  print corpus.empties

  assert len(corpus.empties) > 0

def test_repair_empties():
  corpus = Corpus(dataset_with_errors_dir)

  open(dataset_with_errors_dir+"/187015.md", 'w').close()

  corpus.check()
  corpus.repair()

  open(dataset_with_errors_dir+"/187015.md", 'w').close()

  assert len(corpus.empties) == 0

def test_repair_done():
  corpus_ok = Corpus(dataset_dir)
  corpus_error = Corpus(dataset_with_errors_dir)

  open(dataset_with_errors_dir+"/187015.md", 'w').close()

  corpus_error.check()
  corpus_error.repair()

  event_ok = corpus_ok.read("187015")
  event_repaired = corpus_error.read("187015")

#  open(dataset_with_errors_dir+"/187015.md", 'w').close()

  assert event_ok.content == event_repaired.content