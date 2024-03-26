from settings import *

class Score:
    def __init__(self):
        self.surface = pygame.Surface((SIDEBAR_WIDTH , GAME_HEIGHT*Score_Height_Fraction - Padding))         #((W,H)) , width = 200 , height = 30% of sidebar
        self.display_surface =  pygame.display.get_surface() 