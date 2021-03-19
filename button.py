import pygame

class Button:
    def __init__(self, text, text_size, x, y): 
        self.text = text
        self.text_size = text_size
        self.x = x
        self.y = y
        self.x_border, self.y_border = None, None


    def draw_button(self, screen, colour):

        font = pygame.font.SysFont("georgia", self.text_size)
        text_surface = font.render(self.text, 1, colour)
        text_rect = text_surface.get_rect()

        width = text_rect[2] - text_rect[0]
        height = text_rect[3] - text_rect[1]
        self.x_border = (self.x - width/2, self.x + width/2)
        self.y_border = (self.y - height/2, self.y + height/2)

        text_rect = text_surface.get_rect(center=(self.x, self.y))
        screen.blit(text_surface, text_rect)

        


    def is_over(self, pos):
        
        in_x = self.x_border[0] < pos[0] and pos[0] < self.x_border[1]
        in_y = self.y_border[0] < pos[1] and pos[1] < self.y_border[1]

        if in_x and in_y:
            return True

        else:
            return False



if __name__ == "__main__":

    # import pygame

    menu = Button("Main menu", 80, 450, 150)
    menu.draw_button(WIN)