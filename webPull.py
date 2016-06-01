#!/usr/bin/python
# encoding: utf-8
from lxml import html
import requests
import operator

nameDict = {}
namePubDict = {}
pubs = []
confjournal = []

def pubList(start, end, name, JoC, urlC=None, vols=0):
	weblink = "http://dblp.uni-trier.de/db/"
	if JoC == "j":
		weblink += "journals/"
	else:
		weblink += "conf/"
	if name not in confjournal:
		confjournal.append(name)
	for i in range(start, end):
		if vols == 0:
			if urlC == None:
				pubs.append(
					[weblink+name+"/"+name+str(i)+".html",
						name+str(i)])
			else:
				pubs.append(
					[weblink+urlC+"/"+name+str(i)+".html",
					name+str(i)])
		else:
			if urlC == None:
				for j in range(1, vols+1):
					pubs.append(
						[weblink+name+"/"+name+str(i)+"-"+
						str(j)+".html", name+str(i)+"-"+str(j)])
			else:
				for j in range(1, vols+1):
					pubs.append(
						[weblink+urlC+"/"+name+str(i)+"-"+
						str(j)+".html", name+str(i)+"-"+str(j)])
	

# AI/DM/ML/PR
# 1 - Neural Information Processing Systems (1987-2014)
pubList(1987, 2016, "nips", "c")
# 2 - International Conference of Machine Learning (1993-2015)
pubList(1993, 2016, "icml", "c")
# 3 - Journal of Machine Learning Research (1-16) 5y(12-16)
pubList(1, 17, "jmlr", "j")
# 4 - Artificial Intelligence and Statistics (1995-2015)
pubList(1995, 2016, "aistats", "c")
pubList(1, 24, "jmlrp", "j", "jmlr") # aistats and colt
# 5 - Neural Computation 5y(24-28)
pubList(1, 29, "neco", "j")
# 6 - Uncertainty in Artificial Intelligence (1985-2015)
pubList(1985, 2016, "uai", "c")
# 7 - IEEE Pattern Analysis and Machine Intelligence (1-38) 5y(34-38)
pubList(1, 39, "pami", "j")
# 8 - Conference on Learning Theory
pubList(1988, 2016, "colt", "c")
# 9 - Machine Learning (1-102) 5y(82-102)
pubList(1, 103, "ml", "j")
# 10 - International Joint Conference on Artificial Intelligence
pubList(1969, 2016, "ijcai", "c")
# 11 - AAAI Conference on Artificial Intelligence
pubList(80, 100, "aaai", "c")
pubList(2000, 2016, "aaai", "c")
# 12 - IEEE Transactions on Neural Networks
pubList(1, 28, "tnn", "j")
# 13 - Neural Networks
pubList(1, 78, "nn", "j")
# 14 - Journal of Artificial Intelligence Research
pubList(1, 56, "jair", "j")
# 15 - Artificial Intelligence
pubList(1, 236, "ai", "j")
# 16 - International Conference on Artificial Neural Networks
pubList(1996, 2005, "icann", "c")
pubList(2005, 2012, "icann", "c", vols=2)
# 17 - Neurocomputing
pubList(1, 194, "ijon", "j")
# 18 - ACM Knowledge Discovery and Data Mining (1994-2015)
pubList(94, 100, "kdd", "c")
pubList(2000, 2016, "kdd", "c")
# 19 - IEEE International Conference on Data Mining (ICDM)
pubList(2001, 2016, "icdm", "c")
# 20 - ACM Web Search and Data Mining
pubList(2008, 2017, "wsdm", "c")
# 21 - IEEE Conference on Computer Vision and Pattern Recognition
pubList(1993, 2001, "cvpr", "c")
pubList(2001, 2007, "icann", "c", vols=2)
pubList(2007, 2016, "cvpr", "c")
# 22 - International Conference on Pattern Recognition
pubList(1996, 2000, "icpr", "c")
pubList(2000, 2007, "icpr", "c", vols=4)
pubList(2007, 2015, "icpr", "c")
# 23 - Pattern Recognition
pubList(1, 57, "pr", "j")
# 24 - IEEE Knowledge and Data Engineering (1-28) 5y(24-28)
pubList(1, 29, "tkde", "j")
# 25 - Statistics and Computering
pubList(7, 27, "sac", "j")

# Applications
# 26 - Expert Systems with Applications 5y(38-51)
pubList(20, 51, "eswa", "j")

# 27 - International Conference on Autonomous Agents and Multiagent Systems 
pubList(2002, 2017, "aamas", "c", 'atal')
pubList(2004, 2005, "aamas", "c", 'atal', vols=3)
pubList(2008, 2010, "aamas", "c", 'atal', vols=3)


# 28 - Journal of Computational Neuroscience
pubList(1, 40, "jcns", "j")
# 29 - Cognitive Science
pubList(1, 41, "cogsci", "j")
# 30 - International Conference on Biometrics
pubList(2006, 2016, "icb", "c")
# 31 - Bioinformatics
pubList(1, 33, "bioinformatics", "j")
# 32 - PLoS Computational Biology
pubList(1, 12, "ploscb", "j")
# 33 - IEEE International Conference on Computer Vision
pubList(1987, 1999, "iccv", "c")
pubList(1999, 2006, "iccv", "c", vols=2)
pubList(2006, 2016, "iccv", "c")
# 34 - Computational Linguistics
pubList(1979, 2012, "acl", "c")
pubList(2012, 2016, "acl", "c", vols=2)
# 35 - IEEE International Conference on Acoustics, Speech and Signal Processing
pubList(1976, 2003, "icassp", "c")
pubList(2003, 2008, "icassp", "c", vols=7)
pubList(2008, 2017, "icassp", "c")
# 36 - IEEE Transactions on Fuzzy Systems
pubList(1, 25, "tfs", "j")
# 37 - IEEE International Conference on Robotics and Automation
pubList(1984, 2016, "icra", "c")
# 38 - International World Wide Web Conference
pubList(1994, 2017, "www", "c")
# 39 - Very Large Databases
pubList(1, 42, "vldb", "c")
# 40 - International Conference on Management of Data
pubList(1975, 2016, "sigmod", "c")

profDict = {}
i = 0
for pub in pubs:
	i = i + 1
	page = requests.get(pub[0])
	tree = html.fromstring(page.content)

	names = tree.xpath('//span[@itemprop="name"]/text()')

	print "Processing:",pub[1],i,"out of",len(pubs),"for",len(names)," authors...\n" 

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

# create dataframe with 0s where no pubs
df = DataFrame(nameDict).T.fillna(0)

# create totals column
df['Total'] = df.sum(axis=1)

# filter for those with greater than n pubs
df2 = df[df.Total >= 10]

# reorder columns so total appears first
cols = df2.columns.tolist()
cols = cols[-1:] + cols[:-1]
df3 = df2[cols]

print "Now writing out to csv..."
#df.to_csv("ML_Profs.csv", encoding='utf-8')
df3.to_csv("ML_Profs_full2.csv")

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


