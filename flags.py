#!/usr/local/bin/python

import sys
import re
from colours import colourDict

keywords = ["on","off","switch","colour","status","random","script","circle","ccircle","strobe","fire","disco"]
keywords.extend(colourDict.keys())
print "keywords"

def isFlag(arg):
	print keywords
	return arg.startswith("-") or arg in keywords

def getFlags():
	cmdargs = eval(str(sys.argv))
	
	flagPair={}
	flagPairs=[]
	for arg in cmdargs:	
		if isFlag(arg):
			flagPair={"flag":arg,
				  "args":[]}
			flagPairs.append(flagPair)	
		elif "args" in flagPair:
			flagPair["args"].append(arg)
			
	return flagPairs

