import pygame
from Settings import Settings

class GameFunction:
    def __init__(self, screen, setting: Settings) -> None:
        self.screen = screen
        self.setting = setting
        pass

    def update_screen(self, text, textRect):
        self.screen.fill(self.setting.col_WHITE)
        self.screen.blit(text, textRect)
        pygame.display.flip()