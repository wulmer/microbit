from microbit import *
import random

while True:
    if button_a.was_pressed() or button_b.was_pressed():
        for delay in (10, 20, 50, 100):
            display.show(Image.ALL_CLOCKS, delay)
        number = random.randint(1, 10)
        display.show(str(number))
    else:
        sleep(500)
