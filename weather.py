
import urllib


import os
import socket

import json

from urllib2 import urlopen

def set_lights_by_weather():

    # ip = socket.gethostbyname(socket.gethostname())
    ip = urlopen('http://ip.42.pl/raw').read()

    url = 'https://freegeoip.net/json/{}'.format(ip)

    response = json.loads(urllib.urlopen(url).read())

    lat = response["latitude"]
    lng = response["longitude"]

    forecast = json.loads(urlopen("https://api.forecast.io/forecast/2beeada32fb06ea94f0790895259d23c/{},{}".format(lat, lng)).read())

    print forecast


if __name__ == "__main__":
    set_lights_by_weather()
