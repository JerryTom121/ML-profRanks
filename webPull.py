#!/usr/bin/python
# encoding: utf-8
from lxml import html
import requests
import operator

nameDict = {}
namePubDict = {}
pubs = []

def pubList(start, end, name, JoC):
	weblink = "http://dblp.uni-trier.de/db/"
	if JoC == "j":
		weblink += "journals/"
	else:
		weblink += "conf/"

	for i in range(start, end):
		pubs.append([weblink+name+"/"+name+str(i)+".html",name+str(i)])

# Journal of Machine Learning Research (1-16)
pubList(12, 17, "jmlr", "j")
# IEEE Transactions on Pattern Analysis and Machine Intelligence (1-38)
pubList(34, 39, "pami", "j")
# Machine Learning (1-102)
pubList(80, 103, "ml", "j")
# IEEE Transactions on Knowledge and Data Engineering (1-28)
#pubList(24,29, "tkde", "j")

# Neural Information Processing Systems (1987-2014)
pubList(2010, 2015, "nips", "c")
# International Conference of Machine Learning (1988-2015)
pubList(2011, 2016, "icml", "c")
# ACM Knowledge Discovery and Data Mining (1994-2015)
pubList(2011, 2016, "kdd", "c")
# Artificial Intelligence and Statistics (1995-2015)
#pubList(2011,2016, "aistats", "c")

for pub in pubs:

	page = requests.get(pub[0])
	tree = html.fromstring(page.content)

	names = tree.xpath('//span[@itemprop="name"]/text()')

	for name in names:
	    if name[-1] != '.' and len(name) > 5:
	        if name in nameDict:
	           nameDict[name] += 1
	           namePubDict[name].append(pub[1])
	        else:
	            nameDict[name] = 1
	            namePubDict[name] = [pub[1]]

			


#print nameDict 

sorted_nameDict = sorted(nameDict.items(), 
					key=operator.itemgetter(1),
					reverse=True)

#print sorted_nameDict

#print namePubDict["Michael I. Jordan"]

for tuple in sorted_nameDict:
	if tuple[1] > 10:
		print tuple

