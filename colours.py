#!/usr/local/bin/python
from random import randint

def randomColour():
	return {"bri":randint(0,255),"sat":randint(0,255),"hue":randint(0,65535)}

def colorForHue(hue):
	return {"bri":255,"sat":255,"hue":randint(0,65535)}
	
colorDict = {"red":colorForHue(0)}
	
def getColour(name):
	return colorDict[name]

