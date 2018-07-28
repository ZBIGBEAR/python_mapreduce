#!/usr/bin/env python

import sys

wordDict = {}

for line in sys.stdin:
	line = line.strip()
	word,count = line.split()
	try:
		count = int(count)
	except:
		continue
	
	if word in wordDict:
		wordDict[word] +=1
	else:
		wordDict.setdefault(word,count)

for eachKey in wordDict:
	print(eachKey+'\t'+str(wordDict[eachKey]))
