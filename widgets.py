import pygame

class Button:
    def __init__(self, path, location=[0,0]):
        self.location = location
        self.surface = pygame.image.load(path)
    
    def is_inside(self, mouse):
        height = self.surface.get_height()
        width = self.surface.get_width()
        offset_x = self.location[0]
        offset_y = self.location[1]
        x = mouse[0]
        y = mouse[1]

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

class Switch:
    def __init__(self, paths, location=(0,0)):
        self.location = location
        self.state_count = len(paths)
        self.paths = paths
        self.current_state = 0
        self.surface = pygame.image.load(paths[self.current_state])

    def is_inside(self, mouse):
        height = self.surface.get_height()
        width = self.surface.get_width()
        offset_x = self.location[0]
        offset_y = self.location[1]
        x = mouse[0]
        y = mouse[1]

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
        
    def toggle(self):
        self.current_state = (self.current_state + 1)%self.state_count
        self.surface = pygame.image.load(self.paths[self.current_state])