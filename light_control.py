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
simpleCommands = ["on","off","switch", "colour"]
simpleCommands.extend(colours.colourDict.keys())

for flagPair in flagPairs:
	flag = flagPair["flag"]
	args = flagPair["args"]
	
	if flag == "on":
		requestjson["on"]=True
	elif flag == "off":
		requestjson["on"]=False
	elif flag == "-b":
		requestjson["bri"]=int(args[0])
	elif flag == "-s":
		requestjson["sat"]=int(args[0])
	elif flag == "-h":
		requestjson["hue"]=int(args[0])
	elif flag == "-l":
		lights=args
	elif flag == "status":
		statusDict = getStatus(args)
		for key in statusDict.keys():
			print statusDict[key]
	elif flag == "switch":
		requestjson["on"] = not isAllOn()
	elif flag == "random":
		if len(args)!=0:
			lights=args
		for light in lights:
			sendColorRequest(light, colours.randomColour())
	elif flag == "colour":
		requestjson.update(colours.getColour(args[0]))
	elif flag == "script":
		scripts.playPremadeScript(args[0])
	elif flag == "circle":
		scripts.playCircle()
	elif flag == "ccircle":
		scripts.playChangingCircle()
	elif flag == "strobe":
		scripts.playStrobe()
	elif flag == "fire":
		scripts.playFire()
	elif flag == "disco":
		scripts.playDisco()
	elif flag == "police":
		scripts.playPolice()
	elif flag == "help":
		for keyword in flags.keywords:
			print keyword
	elif flag in colours.colourDict:
		requestjson = colours.getColour(flag)
	if flag in simpleCommands and len(args)!=0:
		lights=args
	
if requestjson:
	sendRequests(lights, requestjson)

