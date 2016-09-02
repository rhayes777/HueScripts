from datetime import datetime
from light_control import *
from time import sleep


def set_lights_by_time():
    time = datetime.now().time()

    second = time.second
    minute = time.minute
    hour = time.hour

    print "second, {}, minute {}, hour {}".format(second, minute, hour)

    minute_color = int(round(65535 * second / 60))
    hour_color = int(round(65535 * (minute + second / 60) / 60))
    day_color = int(round(65535 * (hour + minute / 60 + second / 3600) / 24))

    # print "minute_color {}, hour_color {}, day_color {}".format(minute_color, hour_color, day_color)

    sendColorRequestForHue(lights[0], minute_color)
    sendColorRequestForHue(lights[1], hour_color)
    sendColorRequestForHue(lights[2], day_color)


if __name__ == "__main__":
    while True:
        set_lights_by_time()
        sleep(0.5)
