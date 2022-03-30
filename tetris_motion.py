from microbit import *
import random


class GameOverException(Exception):
    pass


class Piece():
    def __init__(self, x, y, width):
        self.width = width
        self.x = min(max(0, x), 5 - self.width)
        self.y = y

    def move_left(self):
        self.x = max(0, self.x - 1)

    def move_right(self):
        self.x = min(5 - self.width, self.x + 1)

    def drop(self):
        self.y += 1

    def draw(self):
        for i in range(self.width):
            display.set_pixel(self.x + i, self.y, 9)


class Screen():
    def __init__(self):
        self.lines = [[0 for _ in range(5)] for _ in range(5)]

    def can_drop(self, piece):
        if piece.y == 4:
            return False
        elif any([self.lines[piece.y+1][piece.x + w] > 0
                  for w in range(piece.width)]):
            return False
        return True

    def can_move_left(self, piece):
        new_x = max(0, piece.x - 1)
        if self.lines[piece.y][new_x] > 0:
            return False
        return True
        
    def can_move_right(self, piece):
        new_x = min(4, piece.x + 1)
        if self.lines[piece.y][new_x] > 0:
            return False
        return True
        
    def add_piece(self, piece):
        for w in range(piece.width):
            self.lines[piece.y][piece.x + w] = 5

    def remove_full_lines(self):
        removed_lines = 0
        for row in range(4, -1, -1):
            while all([pixel > 0 for pixel in self.lines[row]]):
                for brightness in (0, 9, 0, 9, 0, 9):
                    for x in range(5):
                        display.set_pixel(x, row, brightness)
                        sleep(10)
                self.lines.pop(row)
                self.lines.insert(0, [0 for _ in range(5)])
                removed_lines = removed_lines + 1
        return removed_lines

    def draw(self):
        for row in range(5):
            for col in range(5):
                display.set_pixel(col, row, self.lines[row][col])


class Game(object):
    def __init__(self):
        self.screen = Screen()
        self.piece = None
        self.delay = 100

    def new_piece(self):
        self.piece = Piece(random.randint(0, 4), 0, random.randint(1, 2))

    def draw(self):
        self.screen.draw()
        self.piece.draw()

    def loop(self):
        while True:
            self.new_piece()
            self.draw()
            while True:
                for _ in range(5):
                    if accelerometer.get_x() < -300:
                        if self.screen.can_move_left(self.piece):
                            self.piece.move_left()
                            self.draw()
                    if accelerometer.get_x() > 300:
                        if self.screen.can_move_right(self.piece):
                            self.piece.move_right()
                            self.draw()
                    #if button_a.was_pressed():
                        #self.piece.rotate()
                        #self.draw()
                    #if button_b.was_pressed():
                        #self.piece.rotate()
                        #self.draw()
                    sleep(self.delay)
                if self.screen.can_drop(self.piece):
                    self.piece.drop()
                    self.draw()
                elif self.piece.y == 0:
                    raise GameOverException()
                else:
                    break
            self.screen.add_piece(self.piece)
            removed_lines = self.screen.remove_full_lines()
            if removed_lines:
                self.delay = self.delay * 0.9


while True:
    # wait for player
    idle_counter = 0
    while not button_a.was_pressed() and not button_b.was_pressed():
        sleep(250)
        idle_counter = idle_counter - 1
        if idle_counter < 0:
            idle_counter = 120
            for _ in range(10):
                display.show(Image.ARROW_W)
                sleep(50)
                display.clear()
                sleep(50)
            sleep(500)
            for _ in range(10):
                display.show(Image.ARROW_E)
                sleep(50)
                display.clear()
                sleep(50)
    del idle_counter

    # intro animation
    for i in range(25):
        display.set_pixel(i % 5, int(i / 5), 9)
        sleep(25)
    for i in range(25):
        display.set_pixel(i % 5, int(i / 5), 0)
        sleep(25)

    # run game
    g = Game()
    try:
        g.loop()
    except GameOverException:
        for i in range(25):
            display.set_pixel(i % 5, int(i / 5), 9)
            sleep(25)
        for i in range(25):
            display.set_pixel(i % 5, int(i / 5), 0)
            sleep(25)
        display.scroll('GAME OVER!')
