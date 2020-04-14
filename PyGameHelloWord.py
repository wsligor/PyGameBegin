import pygame
import sys
from pygame.locals import *

from Settings import Settings
from GameFunction import GameFunction

def main():
    pygame.init()

    setting = Settings()
    screen: pygame.Surface = pygame.display.set_mode((setting.sc_height, setting.sc_width))
    pygame.display.set_caption("Привет мир!")

    gf = GameFunction(screen, setting)

    col_WHITE = (255, 255, 255)
    col_BLUE = (0, 0, 255)

    bFont = pygame.font.SysFont(None, 48)
    text: pygame.font.Font = bFont.render('Привет мир!', True, col_BLUE, col_WHITE)
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery

    #screen.fill(col_WHITE)
    #creen.blit(text, textRect)

    #gf.update_screen(text, textRect)

    #pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
        gf.update_screen(text, textRect)

main()



