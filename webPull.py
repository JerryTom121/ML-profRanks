#!/usr/bin/python
# encoding: utf-8
from lxml import html
import requests
import operator

nameDict = {}
namePubDict = {}
pubs = []
confjournal = []

def pubList(start, end, name, JoC):
	weblink = "http://dblp.uni-trier.de/db/"
	if JoC == "j":
		weblink += "journals/"
	else:
		weblink += "conf/"
	if name not in confjournal:
		confjournal.append(name)
	for i in range(start, end):
		pubs.append([weblink+name+"/"+name+str(i)+".html",name+str(i)])
'''
# All-Time Ranks
# Journal of Machine Learning Research (1-16) 5y(12-16)
pubList(1, 17, "jmlr", "j")
# Machine Learning (1-102) 5y(82-102)
pubList(1, 103, "ml", "j")
# IEEE Pattern Analysis and Machine Intelligence (1-38) 5y(34-38)
pubList(1, 39, "pami", "j")
# IEEE Knowledge and Data Engineering (1-28) 5y(24-28)
#pubList(1,29, "tkde", "j")
# Expert Systems with Applications 5y(38-51)
#pubList(1, 51, "eswa", "j")

# International Conference of Machine Learning (1988-2015)
pubList(1988, 2016, "icml", "c")
# Neural Information Processing Systems (1987-2014)
pubList(1987, 2015, "nips", "c")
# AAAI Conference on Artificial Intelligence
pubList(1980, 2016, "aaai", "c")
# Uncertainty in Artificial Intelligence
pubList(1985, 2016, "uai", "c")
# Artificial Intelligence and Statistics (1995-2015)
pubList(1995, 2016, "aistats", "c")
# International Joint Conference on Artificial Intelligence
pubList(1969, 2016, "ijaci", "c")

# ACM Knowledge Discovery and Data Mining (1994-2015)
pubList(1994, 2016, "kdd", "c")
# IEEE International Conference on Data Mining (ICDM)
pubList(2001, 2016, "icdm", "c")
'''

# Last Five Years Ranks
# Journal of Machine Learning Research (1-16) 5y(12-16)
#pubList(12, 17, "jmlr", "j")

# Machine Learning (1-102) 5y(82-102)
#pubList(82, 103, "ml", "j")
# IEEE Pattern Analysis and Machine Intelligence (1-38) 5y(34-38)
#pubList(34, 39, "pami", "j")
# IEEE Knowledge and Data Engineering (1-28) 5y(24-28)
#pubList(24,29, "tkde", "j")
# Expert Systems with Applications 5y(38-51)
#pubList(38, 52, "eswa", "j")

# International Conference of Machine Learning (1988-2015)
pubList(2011, 2016, "icml", "c")
# Neural Information Processing Systems (1987-2014)
pubList(2010, 2015, "nips", "c")
# AAAI Conference on Artificial Intelligence (1980-2015)
#pubList(2011, 2016, "aaai", "c")
# Uncertainty in Artificial Intelligence (1985-2015)
#pubList(2011, 2016, "uai", "c")
# Artificial Intelligence and Statistics (1995-2015)
#pubList(2011, 2016, "aistats", "c")
# International Joint Conference on Artificial Intelligence (1969-2015)
#pubList(2011, 2016, "ijaci", "c")

# ACM Knowledge Discovery and Data Mining (1994-2015)
pubList(2011, 2016, "kdd", "c")
# IEEE International Conference on Data Mining (2001-2015)
#pubList(2011, 2016, "icdm", "c")

profDict = {}

for pub in pubs:

	page = requests.get(pub[0])
	tree = html.fromstring(page.content)

	names = tree.xpath('//span[@itemprop="name"]/text()')

	for name in names:
	    name = name.encode('utf-8')
	    if name[-1] != '.' and len(name) > 5 and "/" not in name:	
	    	if name in nameDict:
	    		if pub[1] in nameDict[name]:
	    			nameDict[name][pub[1]] += 1
	    		else:
	    			nameDict[name][pub[1]] = 1
	    	else:
	    		nameDict[name] = {}
	    		nameDict[name][pub[1]] = 1

#for name in nameDict:
#	print name, nameDict[name]

from pandas import *

df = DataFrame(nameDict).T.fillna(0)

#print df
df.to_csv("test.csv", encoding='utf-8')

'''
	cj = ""
	for char in pub[1]:
		if not char.isdigit():
			cj += char

	print len(names)
	print len(confjournal)

	for name in names:
	    name = name.encode('utf-8')
	    if name[-1] != '.' and len(name) > 5 and "/" not in name:
	        if name in nameDict:
	        	nameDict[name] += 1
	        	namePubDict[name].append(pub[1])
	        	if cj in profDict[name]:
	        		profDict[name]["total"] += 1
	        		profDict[name][cj] += 1
	        	else:
	        		profDict[name]["total"] += 1
	        		profDict[name][cj] = 1
	        else:
	        	nameDict[name] = 1
	        	namePubDict[name] = [pub[1]]
	        	profDict[name] = {}
	        	profDict[name]["total"] = 1
	        	profDict[name][cj] = 1

sorted_nameDict = sorted(nameDict.items(), 
					key=operator.itemgetter(1),
					reverse=True)

#for name in profDict:
#		print name, profDict[name]
#for tuple in sorted_nameDict:
#	if tuple[1] > 10:
#		print tuple[0]+","+str(tuple[1])

#print namePubDict["Michael I. Jordan"]
#print namePubDict["Jieping Ye"]
'''


