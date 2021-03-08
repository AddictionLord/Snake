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

    def __init__(self):
        self.snake = Snake()
        self.main()

    def graphics(self):
        Game.WIN.fill(Game.DARK_BLUE)  # insert tuple with RGB values
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

            self.graphics()

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    s = Snake()
    print(s.x)
    g = Game()
