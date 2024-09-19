class Element_board:
    def __init__(self, r, c, width, height):
        self.c = c
        self.r = r
        self.s = 0
        self.f = False
        self.width = width
        self.height = height

    def display(self):
        stroke(205)
        strokeWeight(0)
        fill(205)
        rect(self.c * self.width, self.r * self.height, self.width, self.height)
