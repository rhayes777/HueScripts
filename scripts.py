#!/usr/local/bin/python

import colours
import bridge_request
import time
from inspect import getargspec
from functools import partial
from random import randint

run = False

def playScript(lightActions, pauseTime = 1):
	bridge_request.turnOn()
	script = Script(lightActions, pauseTime)
	script.run()
	
def playScriptForFunctions(functions, pauseTime = 1, minHue = colours.HUE_MIN, maxHue = colours.HUE_MAX, lightNumbers=[], colourList=[]):
	print "COLOURLIST"
	print colourList
	lightNumbers2, colourList2 = getLightsAndColours()
	if not lightNumbers:
		lightNumbers = lightNumbers2
	if not colourList:
		colourList = colourList2
	print colourList
	lightActions = []
	for function in functions:
		argNames = getargspec(function)[0]
		if "lightNumbers" in argNames:
			function = partial(function, lightNumbers=lightNumbers)
		if "colourList" in argNames:
			function = partial(function, colourList=colourList)
		if "minHue" in argNames:
			function = partial(function, minHue=minHue)
		if "maxHue" in argNames:
			function = partial(function, maxHue=maxHue)
		
		lightActions.append(function)
	playScript(lightActions, pauseTime)
	
def playPremadeScript(scriptNumber):
	print scriptNumber
	if scriptNumber=="0":
		playCircle()
	elif scriptNumber=="1":
		playTwo()
	elif scriptNumber=="2":
		playChangingCircle()
	elif scriptNumber=="3":
		playStrobe()
	elif scriptNumber=="4":
		playFire()
		
def playFire():
	playScriptForFunctions([randomInRangeAction,flashAction],pauseTime=0,minHue=500,maxHue=16000)
		
def playStrobe():
	playScriptForFunctions([flashAction],pauseTime=0.5)
	
def playChangingCircle():
	playScriptForFunctions([changingCircleAction])
	
def playCircle():
	playScriptForFunctions([circleAction])
	
def playTwo():
	playScriptForFunctions([circleAction,flashAction])
	
def playDisco():
	playScriptForFunctions([randomInRangeAction], pauseTime=0.6)

def circleAction(lightNumbers, colourList, t):
	for lightNumber in lightNumbers:
		timeStep = int(lightNumber) + t
		index = timeStep % len(colourList)
		bridge_request.sendColorRequest(lightNumber, colourList[index])
		
def changingCircleAction(lightNumbers, colourList, t):
	colourList[t%len(colourList)] = colours.randomColour()
	circleAction(lightNumbers, colourList, t)
	
def randomInRangeAction(lightNumbers, t, minHue=0, maxHue=65535):
	for lightNumber in lightNumbers:
		bridge_request.sendRequest(lightNumber, colours.randomColourInRange(minHue, maxHue))
		
def randomInSet(lightNumbers, colourList, t):
	for lightNumber in lightNumbers:
		bridge_request.sendRequest(lightNumber, colourList[randint(0, len(colourList)-1)])
		
def flashAction(lightNumbers, t):
	bridge_request.setOn(False, lightNumbers)
	time.sleep(0.4)
	bridge_request.setOn(True, lightNumbers)
	time.sleep(0.2)
	
def randomFlashAction(lightNumbers, t):
	bridge_request.setOn(False, lightNumbers)
	time.sleep(0.4*randint(10)/10)
	bridge_request.setOn(True, lightNumbers)
	time.sleep(0.2*randint(10)/10)
	
def getLightsAndColours():
	lightNumbers = bridge_request.getLightNumbers()
	colourList = []
	for lightNumber in lightNumbers:
		colourList.append(colours.randomColour())
	return lightNumbers, colourList
	
class Script:

	def __init__(self, lightActions, pauseTime = 1):
		self.lightActions = lightActions
		self.t = 0
		self.pauseTime = pauseTime
		
	def run(self):
		run = True
		while run:
			for lightAction in self.lightActions:
				lightAction(t=self.t)
			self.t += 1
			time.sleep(self.pauseTime)
				
		
