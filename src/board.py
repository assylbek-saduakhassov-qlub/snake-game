import random
from .elements import Element_board
from .snake import Snake
from .fruit import Fruit

class Board(list):
    def __init__(self, w, h, rows, columns, width, height):
        self.w = w
        self.h = h
        self.rows = rows
        self.columns = columns
        self.width = width
        self.height = height
        self.score = 0
        self.snake = Snake()
        for row in range(self.rows):
            collection = []
            for column in range(self.columns):
                collection.append(Element_board(row, column, self.width, self.height))
            self.append(collection)

    def snake_into_board(self):
        for element in self.snake:
            if -1 < element.r < self.rows and -1 < element.c < self.columns:
                self[element.r][element.c] = element

    def fruit(self):
        fruit_on_board = 0
        for collection in self:
            for element in collection:
                if element.f != 0:
                    fruit_on_board = 1
        if fruit_on_board == 0:
            r = random.randint(0, self.rows - 1)
            c = random.randint(0, self.columns - 1)
            while self[r][c].f != 0:
                r = random.randint(0, self.rows - 1)
                c = random.randint(0, self.columns - 1)
            self[r][c] = Fruit(r, c, self.width, self.height)

    def display(self):
        if not self.snake.game_over:
            self.fruit()
            self.snake.move(self)
            self.snake_into_board()
            for collection in self:
                for element in collection:
                    element.display()
        else:
            fill(0, 0, 0)
            textSize(40)
            text('GAME OVER!', 180, 300)
            textSize(25)
            text('Score: '+ str(self.snake[-1].s - 3), 250, 350)
