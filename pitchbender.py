from microbit import *
import music

while True:
    music.pitch(abs(accelerometer.get_x()), int(abs(accelerometer.get_y())))