#!/usr/local/bin/python

import requests
import json

def sendRequest(lightNumber,data):
	headers = {'Content-type': 'application/json'}
	r = requests.put("http://192.168.1.64/api/1fd93c561b633f071344f0ba3de5301b/lights/"+str(lightNumber)+"/state", data=json.dumps(data), headers=headers)
	print r.content
	
def sendRequests(lightNumbers,data):
	for lightNumber in lightNumbers:
		sendRequest(lightNumber,data)

def getLights():
	r = requests.get("http://192.168.1.64/api/1fd93c561b633f071344f0ba3de5301b/lights/")
	return r.content

def getStatus(lightNumbers=[]):
	j = json.loads(getLights())
	statusDict = {}
	for key in j.keys():
		status = j[key]["state"]
		if not lightNumbers or key in lightNumbers:
			statusDict[key]=status
	return statusDict

def isLightOn(lightNumbers=[]):
	return isAtleastOneInState("on", True, lightNumbers)
		
def isLightOff(lightNumbers=[]):
	return isAtleastOneInState("on", False, lightNumbers)
	
def isAllOn(lightNumbers=[]):
	return isAllInState("on", True, lightNumbers)

def isAllOff(lightNumbers=[]):
	return isAllInState("on", False, lightNumbers)
	
def isAllInState(key, value, lightNumbers):
	statusDict = getStatus(lightNumbers)
	for lightNumber in lightNumbers:
		if not statusDict[lightNumber][key]==value:
			return False
			
	if not lightNumbers:
		for lightNumber in statusDict.keys():
			if not statusDict[lightNumber][key]==value:
				return False
	return True

def isAtleastOneInState(key, value, lightNumbers=[]):
	statusDict = getStatus(lightNumbers)
	for lightNumber in lightNumbers:
		if statusDict[lightNumber][key]==value:		
			return True
			
	if not lightNumbers:
		for lightNumber in statusDict.keys():
			if statusDict[lightNumber][key]==value:
				return True
	return False
	

