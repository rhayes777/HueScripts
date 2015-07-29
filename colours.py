#!/usr/local/bin/python
from random import randint
import colorsys 

colourGap = 10923
HUE_MAX = 65535
BRI_MAX = 255
SAT_MAX = BRI_MAX
HUE_MIN = 0

def colourForHBS(hue, brightness, saturation):
	return {"bri":brightness,"sat":saturation,"hue":hue}
	
def colourForRGB(red, green, blue):
	hue, brightness, saturation = colorsys.rgb_to_hls(red, green, blue)
	return colourForHBS(int(hue * HUE_MAX), int(brightness * BRI_MAX), int(saturation * SAT_MAX))

def randomColour():
	return colourForHBS(randint(0,HUE_MAX), randint(0,BRI_MAX), randint(0,SAT_MAX))

def colourForHue(hue):
	return colourForHBS(hue, 255, 255)
	
colourDict = {"red":colourForRGB(1, 0, 0),"orange":colourForRGB(0.5, 1, 1),"yellow":colourForRGB(0, 1, 1), "green":colourForRGB(0, 1, 0), "blue":colourForRGB(0, 0, 1)}
	
def getColour(name):
	return colourDict[name]
	
def getHue(name):
	return getColour(name)["hue"]
	
def randomColourInRange(min, max):
	return colourForHue(randint(min, max))
	

	


