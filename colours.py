#!/usr/local/bin/python
from random import randint

colourGap = 10923

def randomColour():
	return {"bri":randint(0,255),"sat":randint(0,255),"hue":randint(0,65535)}

def colorForHue(hue):
	return {"bri":255,"sat":255,"hue":hue}
	
colorDict = {"red":colorForHue(0),"orange":colorForHue(int(colourGap/2)),"yellow":colorForHue(colourGap), "green":colorForHue(2*colourGap)}
	
def getColour(name):
	return colorDict[name]
	
def randomColourInRange(min, max):
	return colorForHue(randint(min, max))
	


