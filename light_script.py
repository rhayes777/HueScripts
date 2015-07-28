#!/usr/local/bin/python

import sys
import re
import flags
import requests
import json

def sendRequest(lightNumber,data):
	headers = {'Content-type': 'application/json'}
	r = requests.put("http://192.168.1.64/api/1fd93c561b633f071344f0ba3de5301b/lights/"+str(lightNumber)+"/state", data=json.dumps(data), headers=headers)
	print r.content

def getLights():
	r = requests.get("http://192.168.1.64/api/1fd93c561b633f071344f0ba3de5301b/lights/")
	return r.content

def getStatus(lightNumbers=[]):
	j = json.loads(getLights())
	statusArray = []
	for key in j.keys():
		status = j[key]["state"]
		status["lightNumber"]=key
		if not lightNumbers:
			statusArray.append(status)
		elif key in lightNumbers:
			statusArray.append(status)
		print key
	
	return statusArray

def isLightOn():
	for status in getStatus():
		if status["on"]:
			return True
	return False

def performSwitch(arg):
	requestjson={}
	if arg == "r":
		for status in getStatus():
			requestjson["on"]= not status["on"]
			requestjson["bri"] = status["bri"]
			requestjson["sat"] = status["sat"]
			requestjson["hue"] = status["hue"]
			lightNumber=status["lightNumber"]
			del status["lightNumber"]
			sendRequest(lightNumber, requestjson)
		requestjson={}	
	elif arg == "e":
		requestjson["on"]= not isLightOn()
	return requestjson

flagPairs = flags.getFlags()
lights = [3,4,5]
requestjson={}

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
		for status in getStatus(args):
			print status
	elif flag == "--switch":
		requestjson = performSwitch(args[0])

for lightNumber in lights:
	if requestjson:
		sendRequest(lightNumber,requestjson)
