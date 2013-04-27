from calenda.event import Event 

def test_scrap():
  event = Event("187021")
  event.scrap()

  assert event.html is not None

def test_parse():
  event = Event("187021")
  event.scrap()
  event.parse()

  assert event.title is not None and \
          event.permalink is not "http://calenda.org/187021" and \
          event.abstract is not None and \
          event.content is not None

def test_parse_error():
  event = Event("000000")
  event.scrap()
  event.parse()

  assert event.title is None and \
          event.abstract is None and \
          event.content is None

def test_no_publisher():
  event = Event("234261")

  event.scrap()
  event.parse()

  assert event.publisher is None

def test_open():
  event = Event("187021")

  event.set_dataset("tests/dataset_sample")

  event.open()

  assert event.title is not None and \
          event.permalink is not "http://calenda.org/187021" and \
          event.abstract is not None and \
          event.content is not None

def test_open_missing():
  event = Event("999999")

  event.set_dataset("tests/dataset_error")
  event.open()

  assert event.is_stored is False

def test_open_misformed():
  event = Event("187015")

  event.set_dataset("tests/dataset_error")
  event.open()

  assert event.content is None