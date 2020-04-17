# -*- coding: utf-8 -*-
import curses
import random
from random import randint
from datetime import datetime


class WheelGame:
    def __init__(self, balance = 20):
        self.balance = balance
        self.wheel = []

    def start(self):
        self.generate_wheel()
        return self.wheel

    def generate_wheel(self):
        for x in range(0, 24):
            self.wheel.append(1)
        for x in range(0, 15):
            self.wheel.append(2)
        for x in range(0, 7):
            self.wheel.append(5)
        for x in range(0, 4):
            self.wheel.append(10)
        for x in range(0, 2):
            self.wheel.append(20)
        for x in range(0, 2):
            self.wheel.append(50)

    def take_turn(self, bet):
        # deduct bet
        self.balance = self.balance - 1

        # spin wheel
        random.seed(datetime.now())
        value = randint(0, len(self.wheel)-1)
        self.wheel[value]

        # if wheel land on bet then
        if self.wheel[value] == bet:
            self.balance = self.balance + (2 * self.wheel[value])

        #print(value)
        return self.balance



if __name__ == "__main__":
    game = SnakeGame(gui = True)
    game.start()
    for _ in range(20):
        game.step(randint(0,3))