# -*- coding: utf-8 -*-

import calenda.parser.search

url = "http://calenda.org/search?q=*:*&primary=fdate&sort=datemisenligne_date&order=desc"

calenda.parser.search.parse(url)
