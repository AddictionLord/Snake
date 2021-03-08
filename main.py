import pygame

WIDTH, HEIGHT = 900, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake!")

ICON = pygame.image.load("icon/snake.png")
pygame.display.set_icon(ICON)

FPS = 60

DARK_BLUE = (0, 0, 75)


def draw_window():
    WIN.fill(DARK_BLUE)  # insert tuple with RGB values
    pygame.display.update()


def main():
    clock = pygame.time.Clock() 
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()

    pygame.quit()

if __name__ == "__main__":
    main()
