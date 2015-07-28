#!/usr/local/bin/python

import colours
import bridge_request
import time

run = False

def playScript(lightActions):
	script = Script(lightActions)
	script.run()
	
def playCircle():
	playScript([circleAction])

def circleAction(lightNumbers, colourList, t):
	n = 0
	for lightNumber in lightNumbers:
		index = (int(lightNumber) + t + n) % len(lightNumbers)
		print "index = " + str(index)
		bridge_request.sendRequest(lightNumber, colourList[index])
		n += 1
	
def getLightsAndColours():
	lightNumbers = bridge_request.getLightNumbers()
	colourList = []
	for lightNumber in lightNumbers:
		colourList.append(colours.randomColour())
	return lightNumbers, colourList
	
class Script:

	def __init__(self, lightActions):
		self.lightNumbers, self. colourList = getLightsAndColours()
		bridge_request.turnOn(self.lightNumbers)
		self.lightActions = lightActions
		self.t = 0
		
	def run(self):
		run = True
		while run:
			for lightAction in self.lightActions:
				lightAction(self.lightNumbers, self.colourList, self.t)
				self.t += 1
				time.sleep(1)
				
		
