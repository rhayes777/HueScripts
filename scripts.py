#!/usr/local/bin/python

import colours
import bridge_request
import time
from functools import partial

run = False

def playScript(lightActions, pauseTime = 1):
	bridge_request.turnOn()
	script = Script(lightActions, pauseTime)
	script.run()
	
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
	lightNumbers, colourList = getLightsAndColours()
	playScript([partial(randomInRangeAction,lightNumbers),partial(flashAction,lightNumbers)],0)
		
def playStrobe():
	lightNumbers, colourList = getLightsAndColours()
	playScript([partial(flashAction,lightNumbers)],0.5)
	
def playChangingCircle():
	lightNumbers, colourList = getLightsAndColours()
	playScript([partial(changingCircleAction,lightNumbers=lightNumbers,colourList=colourList)])
	
def playCircle():
	lightNumbers, colourList = getLightsAndColours()
	playScript([partial(circleAction,lightNumbers=lightNumbers,colourList=colourList)])
	
def playTwo():
	lightNumbers, colourList = getLightsAndColours()
	playScript([partial(circleAction,lightNumbers=lightNumbers,colourList=colourList),partial(flashAction,lightNumbers=[4])])


def circleAction(lightNumbers, colourList, t):
	for lightNumber in lightNumbers:
		timeStep = int(lightNumber) + t
		index = timeStep % len(colourList)
		bridge_request.sendColorRequest(lightNumber, colourList[index])
		
def changingCircleAction(lightNumbers, colourList, t):
	colourList[t%len(colourList)] = colours.randomColour()
	circleAction(lightNumbers, colourList, t)
	
def randomInRangeAction(lightNumbers, t, min=0, max=65535):
	for lightNumber in lightNumbers:
		bridge_request.sendRequest(lightNumber, colours.randomColourInRange(min, max))
		
def flashAction(lightNumbers, t):
	bridge_request.setOn(False, lightNumbers)
	time.sleep(0.4)
	bridge_request.setOn(True, lightNumbers)
	time.sleep(0.2)
	
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
				
		
