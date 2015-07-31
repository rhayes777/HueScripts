#!/usr/local/bin/python

import sys
import re
from colours import colourDict
from ooscripts import lightActions

simpleCommands = ["on","off","switch", "colour"]
keywords = ["status","random","script","circle","ccircle","strobe","fire","disco","police","help"]
simpleCommands.extend(colourDict.keys())
keywords.extend(simpleCommands)
keywords.extend(lightActions.keys())

def isFlag(arg):
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

