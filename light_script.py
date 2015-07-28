#!/usr/local/bin/python

import sys
import flags
import requests
import json
from bridge_request import *

flagPairs = flags.getFlags()
lights = [3,4,5]
requestjson={}
simpleCommands = ["--on","--off","--switch"]

for flagPair in flagPairs:
	flag = flagPair["flag"]
	args = flagPair["args"]
	
	def checkArgs():
		if len(args)!=0:
			lights=args
	
	if flag == "--on":
		requestjson["on"]=True
		checkArgs()
	elif flag == "--off":
		requestjson["on"]=False
		checkArgs()
	elif flag == "-b":
		requestjson["bri"]=int(args[0])
	elif flag == "-s":
		requestjson["sat"]=int(args[0])
	elif flag == "-h":
		requestjson["hue"]=int(args[0])
	elif flag == "-l":
		lights=args
	elif flag == "--status":
		statusDict = getStatus(args)
		for key in statusDict.keys():
			print statusDict[key]
	elif flag == "--switch":
		requestjson["on"] = not isAllOn()
		checkArgs()
		
	if flag in simpleCommands and len(args)!=0:
		lights=args
	
if requestjson:
	sendRequests(lights, requestjson)

