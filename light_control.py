#!/usr/local/bin/python

import sys
from flags import *
import requests
import json
import colours
import scripts
from bridge_request import *
import ooscripts
import signal_setup
import config_file

def printKeywords():
	for keyword in keywords:
			print keyword

flagPairs = getFlags()
singleFlags = []
for flagPair in flagPairs:
	singleFlags.append(flagPair["flag"])
lights = [3,4,5]
requestjson={}
simpleCommands.extend(colours.colourDict.keys())

if len(flagPairs)==0:
	printKeywords()

for flagPair in flagPairs:
	flag = flagPair["flag"]
	args = flagPair["args"]
	
	if flag == "on":
		requestjson["on"]=True
	if flag in [3,4,5]:
		if len(lights)==3:
			lights=[]
		lights.append(flag)
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
# 	elif flag == "police":
# 		scripts.playPolice()
	elif flag == "help":
		printKeywords()
	elif flag in ooscripts.lightActions:
			ooscripts.playScriptForNames(list(set(ooscripts.lightActions).intersection(singleFlags)))
	elif flag in colours.colourDict:
		requestjson = colours.getColour(flag)
	elif flag == "save":
		config_file.addState(getStatus(args))
	elif flag == "load":
		for status in config_file.loadStates()[args[0]]:
			print status
	if flag in simpleCommands and len(args)!=0:
		lights=args
	
if requestjson:
	sendRequests(lights, requestjson)

