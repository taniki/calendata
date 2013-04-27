# Calendata [![Build Status](https://travis-ci.org/taniki/calendata.png)](https://travis-ci.org/taniki/calendata) [![Coverage Status](https://coveralls.io/repos/taniki/calendata/badge.png?branch=master)](https://coveralls.io/r/taniki/calendata)


Calendata is a set of python class and macros written to scrap, parse and store events from [calenda](http://calenda.org) website. It also include a jekyll website to make dataset sharing easy.

[Calenda](http://calenda.org) is a french-based website centralizing annoucements, call for proposals and others informations about Humanities and Social Sciences.

## install

```
$ git clone git://github.com/taniki/calendata.git
$ cd calendata
$ pip install -r _scripts/requirements.txt
```

It will perform better inside a [virtualenv](https://pypi.python.org/pypi/virtualenv).

## use

**Calendata** is mainly a set of classes to make scrapping/parsing/reading more easy but some macros are already available for immediate use.

### build a new dataset

```
$ cd _scripts
$ python scrap_all.py
```

**Warning** : This process is very ressource consuming. In the future, it will only download a ready to use dataset distribution.

## generate a csv file compatible with [cortext manager](http://dashboard.cortext.net)

```
$ cd _scripts
$ python export_cortext.py
```

## test

```
$ nosetests -vw _scripts
```
