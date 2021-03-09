import pygame

class Snake:
    def __init__(self):
        self.__x = 450
        self.__y = 300
        self.__size = 5
        self.__colour = (0, 255, 0) # RGB - Green
        self.__move = [0, 0, 0, 0] # Up, Down, Left, Right


    def draw_snake(self, screen):
        head_rect = pygame.Rect(self.__x, self.__y, 20, 20) # (pos_x, pos_y, width, height)
        pygame.draw.rect(screen, self.__colour, head_rect) # (where_to_draw, colour, object)
        # screen.blit(self.head, (self.x, self.y))

    def set_movement(self, order):
        if order == pygame.K_UP:
            self.__move_up()
        
        if order == pygame.K_DOWN:
            self.__move_down()
        
        if order == pygame.K_LEFT:
            self.__move_left()
        
        if order == pygame.K_RIGHT:
            self.__move_right()


    def movement(self):
        if self.__move[0]:
            self.__go_up()

        elif self.__move[1]:
            self.__go_down()

        elif self.__move[2]:
            self.__go_left()

        elif self.__move[3]:
            self.__go_right()


    def __move_up(self):
        if not self.__move[1]:
            self.__move = [1, 0, 0, 0]

    def __move_down(self):
        if not self.__move[0]:
            self.__move = [0, 1, 0, 0]

    def __move_left(self):
        if not self.__move[3]:
            self.__move = [0, 0, 1, 0]
        
    def __move_right(self):
        if not self.__move[2]:
            self.__move = [0, 0, 0, 1]
       
    def __go_up(self):
        self.__y -= 1

    def __go_down(self):
        self.__y += 1
    
    def __go_left(self):
        self.__x -= 1
    
    def __go_right(self):
        self.__x += 1

    def grow(self):
        self.__size += 1
