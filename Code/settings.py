import pygame

#game size 
Columns = 10
Rows = 20
Cell_Size = 32     #originally 40, incase i need to change it 
GAME_WIDTH, GAME_HEIGHT = Columns * Cell_Size, Rows * Cell_Size


#sidebar size
SIDEBAR_WIDTH = 200
Preview_Height_Fraction = 0.7
Score_Height_Fraction = 1 - Preview_Height_Fraction

#window of the game
Padding = 20       #20 pixels from the window to the other parts
Window_Width = GAME_WIDTH + SIDEBAR_WIDTH + Padding * 3    #padding * 3 - cause between the game and window, between game and sidebar, between sidebar and window
Window_Height = GAME_HEIGHT + Padding * 2       # padding * 2 - between game and bottom of window, between game and top of window



#colors:
Yellow = '#F4DE61'
Red = '#FF0000'
Blue = '#0800FF'
Green = '#55A020'
Purple = '#7E20A0'
Cyan = '#00FAFF'
Orange = '#FF8300'
Gray = '#3A3A3A'
Line_Color = '#FFFFFF'