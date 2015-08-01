import json

def loadConfig():
	with open("config.json", 'r') as f:
		jsonContents = loadContents(f)
		print jsonContents
		return jsonContents["ip"], jsonContents["username"]

def saveConfig(ip, username):
	with open("config.json", 'w+') as f:
	        jsonContents = loadContents(f)
	        jsonContents["ip"]=ip
	        jsonContents["username"]=username
	        f.write(json.dumps(jsonContents))

def loadContents(f):
	contents = f.read()
	if not contents:
		contents = "{}"
	return json.loads(contents)
    