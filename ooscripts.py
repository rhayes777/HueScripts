from colours import *
from bridge_request import *
from time import sleep
from math import *

def getRandomLightsAndColours():
	lightNumbers = bridge_request.getLightNumbers()
	colourList = []
	for lightNumber in lightNumbers:
		colourList.append(colours.randomColour())
	return lightNumbers, colourList

def getCurrentLightsAndColours():
	statusDict = getStatus()
	lightNumbers = statusDict.keys()
	colourList = []
	for lightNumber in lightNumbers:
		colourList.append(statusDict[lightNumber])
	return lightNumbers, colourList

def playScriptForName(name):
	playScriptForNames([name])

def playScriptForNames(names):
	lightNumbers, colourList = getCurrentLightsAndColours()
	Script(lightNumbers, colourList, [lightActions[name] for name in names]).play()

class Script:
	
	def __init__(self, lightNumbers, colourList, lightActions):
		self.lightNumbers = lightNumbers
		self.colourList = colourList
		self.lightActions = lightActions
		self.t = 0
		for lightAction in lightActions:
			lightAction.communalLightNumbers = lightNumbers
			lightAction.communalColourList = colourList
		self.run = False
		
	def play(self):
		self.run = True
		while self.run:
			for lightAction in self.lightActions:
				lightAction.perform(self.t)
			self.t += 1
				
				
class PoliceAction:
	
	def __init__(self, firstLights=[5], secondLights=[3,4]):
		self.firstLights = firstLights
		self.secondLights = secondLights
			
	def perform(self, t):
		isFirstRed = t % 2 == 0
		firstColour = getColour("red") if isFirstRed else getColour("blue")
		secondColour = getColour("blue") if isFirstRed else getColour("red") 
		sendColourRequests(self.firstLights, firstColour)
		sendColourRequests(self.secondLights, secondColour)
		sleep(0.7)
		
class FadeFromSideAction:
	
	def __init__(self, leftLight=5, middleLight=3, rightLight=4, pauseTime=0.2, jump=500):
		self.lights = [leftLight, middleLight, rightLight]
		self.colours = [colourForHueDegrees(0), colourForHueDegrees(180), colourForHueDegrees(360)]
		self.pauseTime = pauseTime
		self.jump = jump
		
	def perform(self, t):
		for n in [0,2]:
			sendRequest(self.lights[n],self.colours[n])
			self.colours[n]=colourForHue(self.colours[n]["hue"] + self.jump*(1 - n))
		if self.colours[0]["hue"]>HUE_MAX:
			self.colours[0]=colourForHueDegrees(0)
		if self.colours[2]["hue"]<HUE_MIN:
		    self.colours[2]=colourForHueDegrees(360)
		sleep(self.pauseTime)
		
class SyncopatedFade:
	def __init__(self, leftLight=5, middleLight=3, rightLight=4, pauseTime=0.2, jump=500):
		self.lights = [leftLight, middleLight, rightLight]
		self.colours = [colourForHueDegrees(0), colourForHueDegrees(120), colourForHueDegrees(240)]
		self.pauseTime = pauseTime
		self.jump = jump
		
	def perform(self, t):
		for n in range (0,3):
			sendRequest(self.lights[n],self.colours[n])
			self.colours[n]=colourForHue(self.colours[n]["hue"] + self.jump)
			if self.colours[n]["hue"]>HUE_MAX:
				self.colours[n]=colourForHueDegrees(0)
		
		sleep(self.pauseTime)
		
class BounceFade(FadeFromSideAction):
	def __init__(self, leftLight=5, middleLight=3, rightLight=4, pauseTime=0.2, jump=500):
		self.fadeFromSideAction = FadeFromSideAction(leftLight, middleLight, rightLight, pauseTime, jump)
		self.jump = jump
		self.middleLight = middleLight
		self.middleColour = colourForHueDegrees(0)
		self.directionCoefficient = 1
		
	def perform(self, t):
		sendRequest(self.middleLight,self.middleColour)
		self.middleColour=colourForHue(self.middleColour["hue"] + self.directionCoefficient*self.jump)
		if self.middleColour["hue"]>HUE_MAX:
			self.middleColour=colourForHueDegrees(360)
			self.directionCoefficient=-1
		if self.middleColour["hue"]<HUE_MIN:
		    self.middleColour=colourForHueDegrees(0)
		    self.directionCoefficient=1
		self.fadeFromSideAction.perform(t)
			
class SinFade:
	def __init__(self, lightNumbers=[3,4,5]):
		self.lightNumbers = lightNumbers
# 		self.colourList=[colourFor]
		
		
		
			
lightActions = {"police": PoliceAction(), "fade": FadeFromSideAction(), "sync": SyncopatedFade(), "bounce":BounceFade()}
	