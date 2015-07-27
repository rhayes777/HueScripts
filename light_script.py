#!/usr/local/bin/python

import sys
import re
import flags
import requests
import json

def sendRequest(lightNumber,data):
	headers = {'Content-type': 'application/json'}
	r = requests.put("http://192.168.1.65/api/1fd93c561b633f071344f0ba3de5301b/lights/"+str(lightNumber)+"/state", data=json.dumps(data), headers=headers)
	print r.content	

flagPairs = flags.getFlags()
requestjson = {}
lights = [3,4,5]

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
print requestjson
for lightNumber in lights:
	sendRequest(lightNumber,requestjson)
