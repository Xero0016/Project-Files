from settings import *

class Game:
    def __init__ (self):
        
        #general setup
        self.surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
        self.display_surface = pygame.display.get_surface()             #getting self.display_surface from 'main' file into this file
        
    def run(self):
        self.display_surface.blit(self.surface , (Padding,Padding))     #blit - BlockImageTransfer, (surface,position(x,y))
        