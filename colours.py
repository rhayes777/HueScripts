#!/usr/local/bin/python
from random import randint
import colorsys 

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

def colourForHueDegrees(hueDegrees):
	return colourForHue(HUE_MAX*hueDegrees/360)
	
colourDict = {"red":colourForHueDegrees(0),"orange":colourForHueDegrees(40),"yellow":colourForHueDegrees(80),"sky":colourForHueDegrees(200),"purple":colourForHueDegrees(280),"pink":colourForHueDegrees(300), "green":colourForHueDegrees(130), "blue":colourForHueDegrees(240),"turquoise":colourForHueDegrees(180),"red2":colourForHueDegrees(360)}
	
def getColour(name):
	return colourDict[name]
	
def getHue(name):
	return getColour(name)["hue"]
	
def randomColourInRange(min, max):
	return colourForHue(randint(min, max))
	
def isOverHueMax(colour):
	return colour["hue"]>HUE_MAX
	
def isUnderHueMin(colour):
	return colour["hue"]<HUE_MIN

	


