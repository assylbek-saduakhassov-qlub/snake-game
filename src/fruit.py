import random
import os

path = os.getcwd()

class Fruit:
    def __init__(self, r, c, width, height):
        self.c = c
        self.r = r
        self.s = 0
        self.f = True
        self.width = width
        self.height = height
        self.fruit_items = ["apple", "banana"]
        self.fruit = random.choice(self.fruit_items)
        self.img = loadImage(path + "/images/" + self.fruit + ".png")

    def display(self):
        image(self.img, self.c * self.width, self.r * self.height)
