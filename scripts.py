#!/usr/local/bin/python

import colours
import bridge_request
import time
from functools import partial

run = False

def playScript(lightActions):
	script = Script(lightActions)
	script.run()
	
def playCircle():
	lightNumbers, colourList = getLightsAndColours()
	playScript([partial(circleAction,lightNumbers=lightNumbers,colourList=colourList)])

def circleAction(lightNumbers, colourList, t):
	for lightNumber in lightNumbers:
		timeStep = int(lightNumber) + t
		index = timeStep % len(colourList)
		bridge_request.sendColorRequest(lightNumber, colourList[index])
	
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
				
		
