#!/usr/local/bin/python

import sys
import re

def isFlag(arg):
	return arg.startswith("-")

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

