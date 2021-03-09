import pygame
import sys
from snk import *
from fruit import *
from cell import *


class Game:
    pygame.init()

    # Screen
    NODE_SIZE = 20
    WIDTH, HEIGHT = 900, 600
    ROWS = HEIGHT / NODE_SIZE
    COMUMNS = WIDTH / NODE_SIZE
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
        self.snake = Snake(Game.NODE_SIZE)
        self.apple = Apple(Game.NODE_SIZE)
        self.node = Node(Game.NODE_SIZE)
        self.main()
       

    def graphics(self, timer):
        Game.WIN.fill(Game.DARK_BLUE)  # insert tuple with RGB values
        self.apple.draw_apple(Game.WIN)

        if timer % 10 == 0:
            self.snake.movement()  

        self.snake.draw_snake(Game.WIN, timer)
        pygame.display.update()


    def main(self):
        clock = pygame.time.Clock() 
        run = True

        # Game loop
        timer = 0
        while run:
            clock.tick(Game.FPS)
            timer += 1
            # print(pygame.time.get_ticks())

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.KEYDOWN:
                    if event.key in Game.arrows:
                        self.snake.set_movement(event.key)

            self.graphics(timer)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    g = Game()
