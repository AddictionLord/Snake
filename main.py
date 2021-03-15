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
    

    def __init__(self, player):
        self.player = player
        self.path = list()
        self.snake = Snake(Game.NODE_SIZE)
        self.apple = Apple(Game.NODE_SIZE, Game.ROWS, Game.COLUMNS, self.snake)
        self.artint = AI(self.snake)

        self.snake.set_movement(pygame.K_RIGHT) if self.player else print("AI")
        self.main()
        

    def graphics(self, timer=0):

        Game.WIN.fill(Game.DARK_BLUE)  # insert tuple with RGB values
        
        
        if timer % 7 == 0:
            self.snake.movement()  
        
        self.snake.draw_snake(Game.WIN, timer)
        self.apple.draw_apple(Game.WIN)
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
            print("Game Over")

    
    def generate_path(self, start, target):
        del self.artint
        self.artint = AI(self.snake)
        self.path = self.artint.A_star(start, target)


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

                if self.player:
                    if event.type == pygame.KEYDOWN:
                        if event.key in Game.arrows:
                            self.snake.set_movement(event.key)

            self.check_eating()
            self.check_collision()
            
            if not self.player:
                snake_head = list(self.snake.get_position())
                apple = list(self.apple.get_position())

                # print("Path: ", self.path)
                if not self.path:
                    self.generate_path(snake_head, apple)

                if self.path[0] == snake_head:
                    try:
                        self.path.remove(snake_head)
                        m_next = self.path[0]
                    except IndexError:
                        self.generate_path(snake_head, apple)
                        m_next = self.path[0]
                else:
                    m_next = self.path[0]

                move = [m_next[0] - snake_head[0], m_next[1] - snake_head[1]]
                self.snake.set_movement(move)

            
            self.graphics(timer)




        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    g = Game(False)
