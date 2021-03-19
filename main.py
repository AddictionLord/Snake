import pygame
import sys
from snk import Snake
from fruit import Apple
from A_Intelligence import AI
from button import *


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
    

    def __init__(self, player): # Set player = True if want to play, otherwise for AI
        self.player = player
        self.path = list()
        self.snake = Snake(Game.NODE_SIZE)
        self.apple = Apple(Game.NODE_SIZE, Game.ROWS, Game.COLUMNS, self.snake)
        self.artint = AI(self.snake)

        self.snake.set_movement(pygame.K_RIGHT) if self.player else print("AI") # This belongs to main_menu
        self.main_menu()
       # self.main()
        

    def main_menu(self):

        # self.menu = Button("Main menu", 80, 450, 150)
        self.buttons = [Button("Main menu", 80, 450, 150),
                        Button("Player", 60, 450, 250),
                        Button("A*", 60, 450, 325),
                        Button("Exit", 60, 450, 420)]


        menu = True
        while menu:

            pos = pygame.mouse.get_pos()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    menu = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        menu = False
                        break

                

            self.graphics(draw="Menu", pos=pos)


    def graphics(self, timer=0, draw=None, pos=None):

        if draw == "Menu":
            Game.WIN.fill((0, 0, 0))
            self.buttons[0].draw_button(Game.WIN, (255, 255, 255))


            if self.buttons[1].x_border == None:
                for button in self.buttons:
                    button.draw_button(Game.WIN, (255, 255, 255))

            for button in self.buttons[1:]:
                if button.is_over(pos):
                    button.draw_button(Game.WIN, (255, 255, 0))
                else:
                    button.draw_button(Game.WIN, (255, 255, 255))

            # self.draw_button("Player", 60, 450, 250)
            # self.draw_button("A*", 60, 450, 325)
            # self.draw_button("Exit", 60, 450, 420)


        else:
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


    def artificial_inttelligence(self):
        snake_head = list(self.snake.get_position())
        apple = list(self.apple.get_position())

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




    def main(self):
        
        clock = pygame.time.Clock() 
        # run = True

        # Game loop
        timer = 0
        while Game.run:
            clock.tick(Game.FPS)
            timer += 1
       
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Game.run = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.main_menu()

                    if self.player:
                        if event.key in Game.arrows:
                            self.snake.set_movement(event.key)

            self.check_eating()
            self.check_collision()
            
            if not self.player:
                self.artificial_inttelligence()

            
            self.graphics(timer)

        pygame.quit()
        sys.exit()



if __name__ == "__main__":
    g = Game(False)

# Set g=Game(True) to play yourself, False for AI
