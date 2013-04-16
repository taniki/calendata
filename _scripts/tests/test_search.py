from calenda.search import Search

test_url = "http://calenda.org/search?q=*:*&primary=fdate&sort=datemisenligne_date&order=desc"

def test_scrap():
  search = Search(test_url)

  search.scrap()

  assert search.current_html is not None and \
          search.pager_next is not None

def test_parse():
  search = Search(test_url)

  search.scrap()
  search.parse()

  assert len(search.current_results) == 20

def test_parse_error():
  search = Search("http://calenda.org")

  search.scrap()
  search.parse()

  assert len(search.current_results) == 0

def test_walk():
  search = Search(test_url)

  search.scrap()
  search.parse()

  temp_current = search.pager_current

  search.walk()

  assert search.pager_current is not temp_current