import pygame

class Button:
    def __init__(self, path, location):
        self.location = location
        self.surface = pygame.image.load(path)
    
    def is_inside(self, mouse):
        height = float(self.surface.get_height())
        width = float(self.surface.get_width())
        offset_x = float(self.location[0])
        offset_y = float(self.location[1])
        x = float(mouse[0])
        y = float(mouse[1])

        #formula from math stack exchange https://math.stackexchange.com/questions/76457/check-if-a-point-is-within-an-ellipse
        term1Top = (x - offset_x - (width/2))**2
        term1Bot = (width/2)**2
        term2Top = (y - offset_y - (height/2))**2
        term2Bot = (height/2)**2
        
        output = (term1Top/term1Bot) + (term2Top/term2Bot)

        #is image inside oval
        if output <= 1 :
            return True
        else:
            return False

