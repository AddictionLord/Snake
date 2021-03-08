import pygame


class Game:
    WIDTH, HEIGHT = 900, 600
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake!")

    ICON = pygame.image.load("icon/snake.png")
    pygame.display.set_icon(ICON)

    FPS = 60

    DARK_BLUE = (0, 0, 75)

    def __init__(self):
        self.main()

    def draw_window(self):
        Game.WIN.fill(Game.DARK_BLUE)  # insert tuple with RGB values
        pygame.display.update()


    def main(self):
        clock = pygame.time.Clock() 
        run = True
        while run:
            clock.tick(Game.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            self.draw_window()

        pygame.quit()

if __name__ == "__main__":
    g = Game()
