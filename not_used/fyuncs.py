import pygame # type: ignore

def click(my_font, screen, count):
    X, Y = screen.get_size()
    x, y = my_font.size(str(count))
    xPos = X/2 - (x/2)
    yPos = Y/2 - (y/2)


    # RENDER YOUR GAME HERE
    #display text
    text_surface = my_font.render(str(count), False, (0, 0, 0))
    screen.blit(text_surface, (xPos,yPos))

