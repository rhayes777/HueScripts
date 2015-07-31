from colours import *
from bridge_request import *
from time import sleep

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

lightActions = {"police": PoliceAction()}
	