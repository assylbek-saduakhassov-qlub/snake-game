from src.board import Board

RESOLUTION = 600
COLUMNS = 20
ROWS = 20
WIDTH = RESOLUTION / COLUMNS
HEIGHT = RESOLUTION / ROWS

board = Board(RESOLUTION, RESOLUTION, ROWS, COLUMNS, WIDTH, HEIGHT)

def setup():
    size(board.w, board.h)
    background(0,0,0)

def draw():
    if frameCount % 12 == 0:
        background(205)
        board.display()
        fill(0, 0, 0)
        textSize(15)
        text('Score: '+ str(board.snake[-1].s - 3), 520, 15)

def mouseClicked():
    background(205)
    for row in range(ROWS):
        for column in range(COLUMNS):
            board[row][column] = Element_board(row, column, WIDTH, HEIGHT)
    board.score = 0
    board.snake.game_over = False
    board.snake = Snake()

def keyPressed():
    if keyCode == LEFT:
        if board.snake.key_handler[RIGHT] == True:
            board.snake.key_handler[LEFT] = False
        else:
            board.snake.key_handler[LEFT] = True
            board.snake.key_handler[RIGHT] = False
            board.snake.key_handler[UP] = False
            board.snake.key_handler[DOWN] = False
    elif keyCode == RIGHT:
        if board.snake.key_handler[LEFT] == True:
            board.snake.key_handler[RIGHT] = False
        else:
            board.snake.key_handler[LEFT] = False
            board.snake.key_handler[RIGHT] = True
            board.snake.key_handler[UP] = False
            board.snake.key_handler[DOWN] = False
    elif keyCode == UP:
        if board.snake.key_handler[DOWN] == True:
            board.snake.key_handler[UP] = False
        else:
            board.snake.key_handler[LEFT] = False
            board.snake.key_handler[RIGHT] = False
            board.snake.key_handler[UP] = True
            board.snake.key_handler[DOWN] = False
    elif keyCode == DOWN:
        if board.snake.key_handler[UP] == True:
            board.snake.key_handler[DOWN] = False
        else:
            board.snake.key_handler[LEFT] = False
            board.snake.key_handler[RIGHT] = False
            board.snake.key_handler[UP] = False
            board.snake.key_handler[DOWN] = True
