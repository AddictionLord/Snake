import pygame

class Snake:
    def __init__(self, size):
        self.nsize = size
        self.__x = 20 # 0 - 45
        self.__y = 15 # 0 - 30
        self.__body = [[self.__x, self.__y],[19, 15],[18, 15],[17, 15],[16, 15]] #Edit to list comprehension
        self.__colour = (0, 255, 0) # RGB - Green
        self.__move = [0, 0, 0, 0] # Up, Down, Left, Right
        self.__move_done = True


    def draw_snake(self, screen, timer):
        if timer % 10 == 0:
            body_new = [[self.__x, self.__y]] 
            
            for i in range(len(self.__body) - 1):
                body_new.append(self.__body[i])
            
            self.__body = body_new.copy()
            self.__move_done = True
            self.update(screen, timer)

        else:
            self.update(screen, timer)
            

    def update(self, screen, timer):
        for i in range(len(self.__body)):
                x_pos = self.nsize * self.__body[i][0] # node_size * x coordinate of body = actual position in pixels
                y_pos = self.nsize * self.__body[i][1]

                rect = pygame.Rect(x_pos, y_pos, self.nsize, self.nsize) # (pos_x, pos_y, width, height)
                pygame.draw.rect(screen, self.__colour, rect) # (where_to_draw, colour, object)


    def set_movement(self, order):
        if order == pygame.K_UP:
            if not self.__move[1]:
                self.__move = [1, 0, 0, 0]
            
        if order == pygame.K_DOWN:
            if not self.__move[0]:
                self.__move = [0, 1, 0, 0]
            
        if order == pygame.K_LEFT:
            if not self.__move[3]:
                self.__move = [0, 0, 1, 0]
            
        if order == pygame.K_RIGHT:
            if not self.__move[2]:
                self.__move = [0, 0, 0, 1]


    def movement(self):
        if self.__move[0] and self.__move_done:
            self.__go_up()

        elif self.__move[1] and self.__move_done:
            self.__go_down()

        elif self.__move[2] and self.__move_done:
            self.__go_left()

        elif self.__move[3] and self.__move_done:
            self.__go_right()

        # self.__move_done = False
    

    def __go_up(self):
        self.__y -= 1

    def __go_down(self):
        self.__y += 1
    
    def __go_left(self):
        self.__x -= 1
    
    def __go_right(self):
        self.__x += 1

    
    def get_position(self):
        return (self.__x, self.__y)

    def get_body(self):
        return self.__body

    def grow(self, position):
        self.__body.append(position)

    def move_not_done(self):
        self.__move_done = False
