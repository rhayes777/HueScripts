#!/usr/bin/env python
import requests
import json
import os
import pwd
from time import sleep

result = requests.get("https://www.meethue.com/api/nupnp")
ip = json.loads(result.content)[0]["internalipaddress"]

username = None
while not username:
	result = requests.post("http://"+ip+"/api",data="""{"devicetype":"hue_scripts_"""+ pwd.getpwuid( os.getuid() )[ 0 ] +""""}""")
	jsonResult = json.loads(result.content)[0]
	if "success" in jsonResult:
		username = jsonResult["success"]["username"]
	else:
		print "Please press link button"
	sleep(1)

with open("config.json", 'w+') as f:
	contents = f.read()
	if not contents:
		contents = "{}"
	jsonContents = json.loads(contents)
	jsonContents["ip"]=ip
	jsonContents["username"]=username
	f.write(json.dumps(jsonContents))

print "Setup complete"
