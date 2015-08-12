import json
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
path = os.path.join(__location__, 'config.json')

def addState(name, state):
	with open(path, 'w+') as f:
		jsonContents = loadContents(f)
		print jsonContents
		jsonContents[name]=state
		f.write(json.dumps(jsonContents))
		
def loadStates():
	with open(path, 'r') as f:
		return loadContents(f)

def loadConfig():
	with open(path, 'r') as f:
		jsonContents = loadContents(f)
		return jsonContents["ip"], jsonContents["username"]

def saveConfig(ip, username):
	with open(path, 'w+') as f:
	        jsonContents = loadContents(f)
	        jsonContents["ip"]=ip
	        jsonContents["username"]=username
	        f.write(json.dumps(jsonContents))

def loadContents(f):
	contents = f.read()
	if not contents:
		contents = "{}"
	return json.loads(contents)
    
