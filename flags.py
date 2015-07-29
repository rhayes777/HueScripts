#!/usr/local/bin/python

import sys
import re

keywords = ["on","off","switch","colour","status","random","script","circle","ccircle","strobe","fire"]

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

