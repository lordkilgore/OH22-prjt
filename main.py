import pygame

win = pygame.display.set_mode((500, 500), flags=pygame.RESIZABLE)
pygame.display.set_caption("app")
# pygame.display.set_icon()

class GUI(object):
    def __init__(self):
        self.self = self

    @staticmethod
    def draw_toolbar():
        pygame.draw.rect(win, [255,0,0], (12, 198, 40, 10), width= 10, border_radius=10)


def refresh():                                                          # the GUI
    win.fill([255, 255, 255])
    GUI.draw_toolbar()
    pygame.display.update()

main = True
while main:
    for event in pygame.event.get():                # if the red "X" button is clicked, the program will close
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()
            
    refresh()
