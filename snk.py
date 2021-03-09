import pygame

class Snake:
    def __init__(self):
        self.x = 450
        self.y = 300
        self.size = 5
        self.colour = (0, 255, 0) #Green
        self.head = pygame.Surface((20, 20))
        self.head.fill(self.colour)

        self.move = [0, 0, 0, 0] # Up, Down, Left, Right


    def grow(self):
        self.size += 1

    def move_up(self):
        if not self.move[1]:
            self.move = [1, 0, 0, 0]


    def move_down(self):
        if not self.move[0]:
            self.move = [0, 1, 0, 0]


    def move_left(self):
        if not self.move[3]:
            self.move = [0, 0, 1, 0]

        
    def move_right(self):
        if not self.move[2]:
            self.move = [0, 0, 0, 1]


    def go_up(self):
        self.y -= 1

    def go_down(self):
        self.y += 1
    
    def go_left(self):
        self.x -= 1
    
    def go_right(self):
        self.x += 1


