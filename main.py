
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2, sqlite3, time, os
from bs4 import BeautifulSoup 
SITE_URL = 'http://************.se/fordon/'
LETTERS = 'FABCDEFGHJKLMNOPRSTUWXYZ'
FORB_WORDS = ['APA', 'ARG', 'ASS', 'BAJ', 'BSS', 'CUC', 'CUK', #91 Stycken
'DUM', 'ETA', 'ETT', 'FAG', 'FAN', 'FEG', 'FEL', 'FEM', 'FES', 'FET', 'FNL', 'FUC', 'FUK', 'FUL',
'GAM', 'GAY', 'GEJ', 'GEY', 'GHB', 'GUD', 'GYN', 'HAT', 'HBT', 'HKH', 'HOR', 'HOT', 'KGB', 'KKK',
'KUC', 'KUF', 'KUG', 'KUK', 'KYK', 'LAM', 'LAT', 'LEM', 'LOJ', 'LSD', 'LUS', 'MAD', 'MAO', 'MEN',
'MES', 'MLB', 'MUS', 'NAZ', 'NRP', 'NSF', 'NYP', 'OND', 'OOO', 'ORM', 'PAJ', 'PKK', 'PLO', 'PMS',
'PUB', 'RAP', 'RAS', 'ROM', 'RPS', 'RUS', 'SEG', 'SEX', 'SJU', 'SOS', 'SPY', 'SUG', 'SUP', 'SUR',
'TBC', 'TOA', 'TOK', 'TRE', 'TYP', 'UFO', 'USA', 'WAM', 'WAR', 'WWW', 'XTC', 'XTZ', 'XXL', 'XXX']

def parse(url):
	soup = BeautifulSoup(urllib2.urlopen(url))
	for node in soup.findAll("div", { "class":"tt" }):
		a = ''.join(node.findAll(text=True))
		data.append(a.strip())
	for node in soup.findAll("div", { "class":"tr" }):
		a = ''.join(node.findAll(text=True))
		register.append(a.strip())

def legitUrl(url):
	try:
		urllib2.urlopen(url)
		return True
		pass
	except urllib2.HTTPError as e:
		print e.code 

def saveDb(data):
	conn = sqlite3.connect('example.db')
	c = conn.cursor()
  	c.execute('INSERT INTO CARINFO (REGNR, CHASSINR, FORDAR, STATUS, ANTAGARE, IMPORT, FREG, ITRAFIK, MIL, SBES, NBES) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', data[:11])
  	conn.commit()
	

for FIRST in LETTERS:
	for SEC in LETTERS:
		for THIRD in LETTERS:
			if FIRST + SEC + THIRD in FORB_WORDS:
				print FIRST + SEC + THIRD
			else:
				for x in xrange(0,1000):
					data = []
					register = []
					y = '%03d' % x
					REGNR = FIRST + SEC + THIRD + str(y)
					print REGNR	
					if legitUrl(SITE_URL + REGNR):
						parse(SITE_URL + REGNR)
						saveDb(data)
						os.system('clear')
						for x in xrange(0, len(register)):
							print register[x] + " = " + data[x]
							
					else:
						time.sleep(1)

conn.close()