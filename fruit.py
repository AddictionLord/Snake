import pygame
import random as r
from snk import *

class Apple:
    def __init__(self, size, rows, cols, snake):
        self.size = size
        self.snake = snake
        self.rows = rows
        self.cols = cols
        self.__x, self.__y = self.generate_position() 
        self.__colour = (255, 0, 0) # RGB - Red

    # This could slow the game down if snake occupy most game nodes
    def generate_position(self):

        position = [r.randint(0, self.cols - 1), r.randint(0, self.rows - 1)]
        if position in self.snake.get_body():
            position[0], position[1] = self.generate_position()

        return position[0], position[1]


    def draw_apple(self, screen):

        x_pos = self.size * self.__x
        y_pos = self.size * self.__y

        apple_rect = pygame.Rect(x_pos, y_pos, self.size, self.size) # (pos_x, pos_y, width, height)
        pygame.draw.ellipse(screen, self.__colour, apple_rect) # (where_to_draw, colour, object)


    def get_position(self):

        return (self.__x, self.__y)
