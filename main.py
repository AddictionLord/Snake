import pygame
import sys
from snk import *


class Game:
    pygame.init()

    # Screen
    WIDTH, HEIGHT = 900, 600
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))

    # Title
    pygame.display.set_caption("Snake!")

    # Icon
    ICON = pygame.image.load("icon/snake.png")
    pygame.display.set_icon(ICON)

    FPS = 60
    DARK_BLUE = (0, 0, 75) # RGB Values
    arrows = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
    

    def __init__(self):
        self.snake = Snake()
        self.main()

    def movement(self, order):
        if order == pygame.K_LEFT:
            move
        pass
        

    def graphics(self):
        Game.WIN.fill(Game.DARK_BLUE)  # insert tuple with RGB values
        # self.movement()
        Game.WIN.blit(self.snake.head, (self.snake.x, self.snake.y))
        pygame.display.update()


    def main(self):
        clock = pygame.time.Clock() 
        run = True

        # Game loop
        while run:
            clock.tick(Game.FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.KEYDOWN:
                    if event.key in Game.arrows:
                        self.movement(event.key)

            self.graphics()

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    g = Game()
