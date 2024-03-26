from settings import *
from sys import exit

#components
from game import Game

#the window
class Main:
    def __init__(self):
        
        #general setup
        pygame.init()
        self.display_surface = pygame.display.set_mode((Window_Width,Window_Height))   #displaying the window with the width and height
        self.clock = pygame.time.Clock()                                                        #used to work with time in pygame
        pygame.display.set_caption('TETRIS')                    #Title of the Window
        
        
        #components
        self.game = Game()                              #instance of game class
        
        
    def run(self):
        while True:
            for event in pygame.event.get():            #gets all the user inputs
                if event.type == pygame.QUIT:            #tells the pygame if we want to quit
                    pygame.quit()
                    exit()                                 #exit everything, i.e doesnt run anything anymore                    
            
            #display
            self.display_surface.fill(Gray)                 #color of the window
            
            self.game.run()                                 #displaying game area
            
            #updating the game
            pygame.display.update()             #updates what the user does in game so we can see it
            self.clock.tick()                   #used to control fps, if self.clock.tick(60) then game run at 60 frames per sec, but now set to run as fast as possible
        
if __name__ == '__main__':
    main = Main()
    main.run()