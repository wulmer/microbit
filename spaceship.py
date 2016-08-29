from microbit import *
import random

class Ship():
    def __init__(self, pos):
        self._pos = pos
        self.clear()
        self.draw()
    def draw(self):
        display.set_pixel(self._pos, 4, 9)
    def clear(self):
        for i in range(5):
            display.set_pixel(i, 4, 0)
    def right(self):
        self.clear()
        self._pos = min(4, self._pos + 1)
        self.draw()
    def left(self):
        self.clear()
        self._pos = max(0, self._pos - 1)
        self.draw()
        
        
class Space():
    def __init__(self):
        self.lines = [[0 for i in range(5)] for j in range(4)]
    def scroll(self):
        for i in range(3, 0, -1):
            self.lines[i] = self.lines[i-1]
        self.lines[0] = [(random.randint(0, 9) > 8) for i in range(5)]
    def draw(self):
        for row, line in enumerate(self.lines):
            for col in range(5):
                display.set_pixel(col, row, self.lines[row][col] * 2)
    def check_collision(self, ship):
        if self.lines[3][ship._pos] > 0:
            return True
    
ship = Ship(2)
space = Space()
advance_space = False
while True:
    if advance_space:
        space.scroll()
        space.draw()
    else:
        advance_space = not advance_space
    if button_a.was_pressed():
        ship.left()
    elif button_b.was_pressed():
        ship.right()
    if space.check_collision(ship):
        display.show(Image.SKULL)
        break
    sleep(200)