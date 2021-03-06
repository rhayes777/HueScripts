#!/usr/local/bin/python

import requests
import json
import config_file

isLogging = False

ip, username = config_file.loadConfig()
lightsUrl = "http://" + ip + "/api/" + username + "/lights/"


def log(message):
    if isLogging:
        print "bridge_request: " + str(message)


def sendColorRequestForHue(lightNumber, hue):
    sendColorRequest(lightNumber, {"on": True, "bri": 255, "sat": 255, "hue": hue})


def sendColourRequests(lightNumbers, colour):
    for lightNumber in lightNumbers:
        sendColorRequest(lightNumber, colour)


def sendColorRequest(lightNumber, colour, on=True):
    colour["on"] = on
    sendRequest(lightNumber, colour)


# lightNumber - integer key for light (3,4,5)
# data = anyof{"on":True,"bri":255,"sat":255,"hue":65000 or something like that } 
def sendRequest(lightNumber, data, on=True):
    if not "on" in data:
        data["on"] = on
    print "light " + str(lightNumber) + ": "
    for key in data.keys():
        print key + " = " + str(data[key]) + " "
    headers = {'Content-type': 'application/json'}
    r = requests.put(lightsUrl + str(lightNumber) + "/state", data=json.dumps(data), headers=headers)
    if not 200 <= r.status_code < 300:
        print r.content


def sendRequests(lightNumbers, data, on=True):
    for lightNumber in lightNumbers:
        sendRequest(lightNumber, data, on)


def getLights():
    r = requests.get(lightsUrl)
    return r.content


def getLightNumbers():
    return json.loads(getLights()).keys()


def turnOn(lightNumbers=[]):
    if not lightNumbers:
        lightNumbers = getLightNumbers()
    sendRequests(lightNumbers, {"on": True})


def turnOff(lightNumbers=[]):
    if not lightNumbers:
        lightNumbers = getLightNumbers()
    sendRequests(lightNumbers, {}, on=False)


def setOn(isOn, lightNumbers=[]):
    if not lightNumbers:
        lightNumbers = getLightNumbers()
    sendRequests(lightNumbers, {"on": isOn})


def getLightCount():
    j = json.loads(getLights())
    statusDict = {}
    n = 0
    for key in j.keys():
        n += 1
    return n


def getStatus(lightNumbers=[]):
    j = json.loads(getLights())
    statusDict = {}
    for key in j.keys():
        status = j[key]["state"]
        if not lightNumbers or key in lightNumbers:
            statusDict[key] = status
    return statusDict


def isLightOn(lightNumbers=[]):
    return isAtleastOneInState("on", True, lightNumbers)


def isLightOff(lightNumbers=[]):
    return isAtleastOneInState("on", False, lightNumbers)


def isAllOn(lightNumbers=[]):
    return isAllInState("on", True, lightNumbers)


def isAllOff(lightNumbers=[]):
    return isAllInState("on", False, lightNumbers)


def isAllInState(key, value, lightNumbers):
    statusDict = getStatus(lightNumbers)
    for lightNumber in lightNumbers:
        if not statusDict[lightNumber][key] == value:
            return False

    if not lightNumbers:
        for lightNumber in statusDict.keys():
            if not statusDict[lightNumber][key] == value:
                return False
    return True


def isAtleastOneInState(key, value, lightNumbers=[]):
    statusDict = getStatus(lightNumbers)
    for lightNumber in lightNumbers:
        if statusDict[lightNumber][key] == value:
            return True

    if not lightNumbers:
        for lightNumber in statusDict.keys():
            if statusDict[lightNumber][key] == value:
                return True
    return False
