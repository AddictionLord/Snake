import pygame
import random as r

class Apple:
    def __init__(self):
        self.x = r.randint(0, 900)
        self.y = r.randint(0, 600)
        self.colour = (255, 0, 0) # RGB - Red

    def draw_apple(self, screen):
        apple_rect = pygame.Rect(self.x, self.y, 20, 20) # (pos_x, pos_y, width, height)
        pygame.draw.ellipse(screen, self.colour, apple_rect) # (where_to_draw, colour, object)
