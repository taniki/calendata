from calenda.parser.event import Event 

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

def test_open():
  event = Event("187021")

  event.set_dataset("../_dataset")

  event.open()
  
  assert event.title is not None and \
          event.permalink is not "http://calenda.org/187021" and \
          event.abstract is not None and \
          event.content is not None