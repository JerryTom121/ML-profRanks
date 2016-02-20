#!/usr/bin/python
# encoding: utf-8
from lxml import html
import requests
import operator

nameDict = {}
pubs = []

def pubList(start, end, name, JoC):
	weblink = "http://dblp.uni-trier.de/db/"
	if JoC == "j":
		weblink += "journals/"
	else:
		weblink += "conf/"

	for i in range(start, end):
		pubs.append(weblink+name+"/"+name+str(i)+".html")

pubList(7, 17, "jmlr", "j")
pubList(29, 39, "pami", "j")
pubList(66, 103, "ml", "j")
pubList(32, 51, "eswa", "j")
pubList(2005, 2015, "nips", "c")
pubList(2006, 2016, "icml", "c")
pubList(2006, 2016, "kdd", "c")
pubList(2006, 2016, "cvpr", "c")

for pub in pubs:

	page = requests.get(pub)
	tree = html.fromstring(page.content)

	names = tree.xpath('//span[@itemprop="name"]/text()')

	for name in names:
	    if name[-1] != '.' and len(name) > 5:
	        if name in nameDict:
	           nameDict[name] += 1
	        else:
	            nameDict[name] = 1

#print nameDict 

sorted_nameDict = sorted(nameDict.items(), 
					key=operator.itemgetter(1),
					reverse=True)

#print sorted_nameDict

for tuple in sorted_nameDict:
	if tuple[1] > 25:
		print tuple

