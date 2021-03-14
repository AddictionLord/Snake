import pygame
import sys
from snk import *
from fruit import *
from A_Intelligence import *


class Game:
    pygame.init()

    # Screen
    NODE_SIZE = 20
    WIDTH, HEIGHT = 900, 600
    ROWS = HEIGHT / NODE_SIZE
    COLUMNS = WIDTH / NODE_SIZE
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))

    # Title
    pygame.display.set_caption("Snake!")

    # Icon
    ICON = pygame.image.load("icon/snake.png")
    pygame.display.set_icon(ICON)

    run = True
    FPS = 60
    DARK_BLUE = (0, 0, 75) # RGB Values
    arrows = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
    

    def __init__(self):
        self.snake = Snake(Game.NODE_SIZE)
        self.apple = Apple(Game.NODE_SIZE, Game.ROWS, Game.COLUMNS, self.snake)
        self.snake.set_movement(pygame.K_RIGHT)
        self.main()
        

    def graphics(self, timer=0):

        Game.WIN.fill(Game.DARK_BLUE)  # insert tuple with RGB values
        self.apple.draw_apple(Game.WIN)
        
        if timer % 7 == 0:
            self.snake.movement()  
        
        self.snake.draw_snake(Game.WIN, timer)
        pygame.display.update()


    def check_eating(self):

        if self.apple.get_position() == self.snake.get_position():
            self.snake.grow(self.apple.get_position())
            del self.apple
            self.apple = Apple(Game.NODE_SIZE, Game.ROWS, Game.COLUMNS, self.snake)


    def check_collision(self):

        snake_head = list(self.snake.get_position())
        out_of_map = snake_head[0] < 0 or snake_head[0] > 44 or snake_head[1] < 0 or snake_head[1] > 29  
        snake_body = self.snake.get_body()
        if snake_head in snake_body or out_of_map:
            Game.run = False


    def main(self):
        
        clock = pygame.time.Clock() 
        run = True

        # Game loop
        timer = 0
        while Game.run:
            clock.tick(Game.FPS)
            timer += 1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Game.run = False

                if event.type == pygame.KEYDOWN:
                    if event.key in Game.arrows:
                        self.snake.set_movement(event.key)

            self.check_eating()
            self.check_collision()
                
            self.graphics(timer)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    g = Game()
