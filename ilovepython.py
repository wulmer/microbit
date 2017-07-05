import speech
from microbit import *

while True:
    if button_a.was_pressed():
        display.show('I', wait=False)
        speech.pronounce('AY', speed=100, pitch=72)
        sleep(1000)
        display.show(Image.HEART, wait=False)
        speech.pronounce('LAHV', speed=150, pitch=72)
        sleep(1000)
        display.scroll('Python', wait=False)
        speech.pronounce('PAY3THAAN', speed=100, pitch=72)
        sleep(5000)
        display.show(Image.HAPPY)
    elif button_b.was_pressed():
        display.scroll('Hello', wait=False)
        speech.pronounce('/HEH3LOW', speed=100, pitch=72)
    sleep(500)