from microbit import *

while True:
    display.show(Image.ASLEEP)
    z = accelerometer.get_z()
    if z > -900 and not button_a.is_pressed():
        for i in range(3):
            display.show(Image.ANGRY)
            sleep(100)
            display.clear()
            sleep(50)
    sleep(200)    
