#!/usr/local/bin/python

import sys
import flags
import requests
import json
import colours
from bridge_request import *

flagPairs = flags.getFlags()
lights = [3,4,5]
requestjson={}
simpleCommands = ["--on","--off","--switch", "--collor"]

for flagPair in flagPairs:
	flag = flagPair["flag"]
	args = flagPair["args"]
	
	if flag == "--on":
		requestjson["on"]=True
	elif flag == "--off":
		requestjson["on"]=False
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
	elif flag == "--random":
		if len(args)!=0:
			lights=args
		for light in lights:
			sendRequest(light, colours.randomColour())
	elif flag == "--colour":
		requestjson.update(colours.getColour(args[0]))
		
	if flag in simpleCommands and len(args)!=0:
		lights=args
	
if requestjson:
	sendRequests(lights, requestjson)

