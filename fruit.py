import pygame
import random as r

class Apple:
    def __init__(self, size):
        self.size = size
        self.__x = r.randint(0, 45)
        self.__y = r.randint(0, 30)
        self.__colour = (255, 0, 0) # RGB - Red

    def draw_apple(self, screen):
        x_pos = self.size * self.__x
        y_pos = self.size * self.__y

        apple_rect = pygame.Rect(x_pos, y_pos, self.size, self.size) # (pos_x, pos_y, width, height)
        pygame.draw.ellipse(screen, self.__colour, apple_rect) # (where_to_draw, colour, object)
