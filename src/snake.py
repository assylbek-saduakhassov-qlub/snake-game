import random
from .elements import Element_board

class Snake(list):
    def __init__(self):
        self.game_over = False
        self.append(Element_snake(9, 11, 1))
        self.append(Element_snake(9, 10, 2))
        self.append(Element_snake(9, 9, 3,))
        self.key_handler = {LEFT:False, RIGHT:True, UP:False, DOWN:False}

    def head_move(self, head, board):
        head = head
        if self.key_handler[LEFT]:
            head.c = head.c - 1
            if head.c > -1:
                self.eat(head.r, head.c, board)
            for tail in self:
                if tail.r == head.r and tail.c == head.c and tail.s != 1:
                    board.snake.game_over = True
            self[0] = head
            head.head = LEFT
        elif self.key_handler[RIGHT]:
            head.c = head.c + 1
            self[0] = head
            if head.c < 20:
                self.eat(head.r, head.c, board)
            for tail in self:
                if tail.r == head.r and tail.c == head.c and tail.s != 1:
                    board.snake.game_over = True
            head.head = RIGHT
        elif self.key_handler[UP]:
            head.r = head.r - 1
            self[0] = head
            if head.r > -1:
                self.eat(head.r, head.c, board)
            for tail in self:
                if tail.r == head.r and tail.c == head.c and tail.s != 1:
                    board.snake.game_over = True
            head.head = UP
        elif self.key_handler[DOWN]:
            head.r = head.r + 1
            self[0] = head
            if head.r < 20:
                self.eat(head.r, head.c, board)
            for tail in self:
                if tail.r == head.r and tail.c == head.c and tail.s != 1:
                    board.snake.game_over = True
            head.head = DOWN

    def move(self, board):
        for head in self:
            if head.s == 1 and head.c < board.columns and head.r < board.rows and head.c > -1 and head.r > -1:
                current_tail = 2
                empty_row = head.r
                empty_col = head.c
                self.head_move(head, board)
                tail_numbers = 0
                for element in self:
                    if element.s > tail_numbers:
                        tail_numbers = element.s
                while current_tail != tail_numbers + 1:
                    for tail in self:
                        if tail.s == current_tail:
                            if tail.f == False:
                                self[tail.s - 1] = Element_snake(empty_row, empty_col, tail.s)
                            elif tail.f:
                                self[tail.s - 1] = Element_snake(empty_row, empty_col, tail.s, True, tail.fruit)
                                board.fruit()
                            empty_row = tail.r
                            empty_col = tail.c
                            current_tail = current_tail + 1
                            board[tail.r][tail.c] = Element_board(tail.r, tail.c, board.width, board.height)
                break
            elif head.s == 1:
                self.game_over = True

    def eat(self, row, col, board):
        fruit_r = row
        fruit_c = col
        if board[fruit_r][fruit_c].f:
            last_tail = self[-1]
            self.append(Element_snake(last_tail.r, last_tail.c, last_tail.s + 1, True, board[fruit_r][fruit_c].fruit))
            board[fruit_r][fruit_c] = Element_board(fruit_r, fruit_c, board.width, board.height)
