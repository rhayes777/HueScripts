#!/usr/local/bin/python

import sys
import re
from colours import colourDict
from ooscripts import lightActions

simpleCommands = ["on","off","switch", "colour"]
keywords = ["status","random","circle","ccircle","strobe","fire","disco","police","help","save","fingers"]
lightNames = ["window", "tv", "sofa"]
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
		arg = arg.lower()
		if isFlag(arg):
			flagPair={"flag":arg,
				  "args":[]}
			flagPairs.append(flagPair)	
		elif "args" in flagPair:
			if arg.lower() in lightNames:
				arg = lightNames.index(arg)+3
			flagPair["args"].append(arg)
			
	return flagPairs

