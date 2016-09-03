from datetime import datetime, timedelta
import urllib
import json
from urllib2 import urlopen
import colours
from bridge_request import sendColorRequest
from light_control import lights
from math import ceil


CLEAR_DAY = "clear-day"
CLEAR_NIGHT = "clear-night"
RAIN = "rain"
SNOW = "snow"
SLEET = "sleet"
WIND = "wind"
FOG = "fog"
CLOUDY = "cloudy"
PARTLY_CLOUDY_DAY = "partly-cloudy-day"
PARTLY_CLOUDY_NIGHT = "partly-cloudy-night"


class WeatherColor:

    def __init__(self, icon, color):
        self.icon = icon
        self.color = colours.colourDict[color]


weather_colors = \
    [
        WeatherColor(CLEAR_DAY, "yellow"),
        WeatherColor(CLEAR_NIGHT, "yellow"),
        WeatherColor(RAIN, "blue"),
        WeatherColor(SNOW, "blue"),
        WeatherColor(SLEET, "blue"),
        WeatherColor(FOG, "white"),
        WeatherColor(CLOUDY, "white"),
        WeatherColor(PARTLY_CLOUDY_DAY, "white"),
        WeatherColor(PARTLY_CLOUDY_NIGHT, "white")
        ]


def set_lights_by_weather():

    ip = urlopen('http://ip.42.pl/raw').read()

    url = 'https://freegeoip.net/json/{}'.format(ip)

    location_json = json.loads(urllib.urlopen(url).read())

    lat = location_json["latitude"]
    lng = location_json["longitude"]

    weather_json = json.loads(urlopen("https://api.forecast.io/forecast/2beeada32fb06ea94f0790895259d23c/{},{}".format(lat, lng)).read())

    daily_forecasts = weather_json["daily"]["data"]

    tomorrow = (datetime.now() + timedelta(days=1)).date()

    for day_forecast in daily_forecasts:
        if (datetime.utcfromtimestamp(day_forecast["time"])).date() == tomorrow:
            temperature = (day_forecast["temperatureMax"] + day_forecast["temperatureMin"]) / 2
            precip_intensity = day_forecast["precipIntensity"]
            icon = day_forecast["icon"]

            temp_color_degrees = int((100 - temperature) * 2.4)

            if temp_color_degrees > 240:
                temp_color_degrees = 240
            elif temp_color_degrees < 0:
                temp_color_degrees = 0

            precip_brightness = int(ceil(255 * float(precip_intensity) / 75))

            temp_color = colours.colourForHueDegrees(temp_color_degrees)
            icon_color = filter(lambda weather_color: weather_color.icon == icon, weather_colors)[0].color
            precip_color = colours.colourDict["blue"]
            precip_color["bri"] = precip_brightness

            sendColorRequest(lights[0], temp_color)
            sendColorRequest(lights[1], icon_color)
            sendColorRequest(lights[2], precip_color)



if __name__ == "__main__":
    set_lights_by_weather()
