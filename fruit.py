import pygame
import random as r

class Apple:
    def __init__(self, size, rows, cols):
        self.size = size
        self.__x = r.randint(0, cols - 1)
        self.__y = r.randint(0, rows - 1)
        self.__colour = (255, 0, 0) # RGB - Red

    def draw_apple(self, screen):
        x_pos = self.size * self.__x
        y_pos = self.size * self.__y

        apple_rect = pygame.Rect(x_pos, y_pos, self.size, self.size) # (pos_x, pos_y, width, height)
        pygame.draw.ellipse(screen, self.__colour, apple_rect) # (where_to_draw, colour, object)

    def get_position(self):
        return (self.__x, self.__y)
