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

        self.up = False
        self.down = False
        self.left = False
        self.right = False


    def grow(self):
        self.size += 1

    def move_up(self):
        if not self.down:
            self.up = True
            self.down = False
            self.left = False
            self.right = False


    def move_down(self):
        if not self.up:
            self.up = False
            self.down = True
            self.left = False
            self.right = False


    def move_left(self):
        if not self.right:
            self.up = False
            self.down = False
            self.left = True
            self.right = False

        
    def move_right(self):
        if not self.left:
            self.up = False
            self.down = False
            self.left = False
            self.right = True


    def go_up(self):
        self.y -= 1

    def go_down(self):
        self.y += 1
    
    def go_left(self):
        self.x -= 1
    
    def go_right(self):
        self.x += 1


