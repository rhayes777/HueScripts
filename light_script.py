#!/usr/local/bin/python

import sys
import flags
import requests
import json
import colours
import scripts
from bridge_request import *

flagPairs = flags.getFlags()
lights = [3,4,5]
requestjson={}
simpleCommands = ["--on","--off","--switch", "--colour"]

for flagPair in flagPairs:
	flag = flagPair["flag"]
	args = flagPair["args"]
	
	if flag in "--on":
		requestjson["on"]=True
	elif flag in "--off":
		requestjson["on"]=False
	elif flag in "-b":
		requestjson["bri"]=int(args[0])
	elif flag in "-s":
		requestjson["sat"]=int(args[0])
	elif flag in "-h":
		requestjson["hue"]=int(args[0])
	elif flag in "-l":
		lights=args
	elif flag in "--status":
		statusDict = getStatus(args)
		for key in statusDict.keys():
			print statusDict[key]
	elif flag in "--switch":
		requestjson["on"] = not isAllOn()
	elif flag in "--random":
		if len(args)!=0:
			lights=args
		for light in lights:
			sendColorRequest(light, colours.randomColour())
	elif flag in "--colour":
		requestjson.update(colours.getColour(args[0]))
	elif flag in "--script":
		scripts.playPremadeScript(args[0])
	if flag in simpleCommands and len(args)!=0:
		lights=args
	
if requestjson:
	sendRequests(lights, requestjson)

