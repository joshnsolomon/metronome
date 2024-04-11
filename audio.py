import pygame

class Beats:
    # might have to change this to pygame.mixer.find_channel()
    pygame.mixer.init()
    channel = pygame.mixer.Channel(1)

    hat =   pygame.mixer.Sound("./sounds/HAT.wav")
    snare = pygame.mixer.Sound("./sounds/SNARE.wav")
    rim =   pygame.mixer.Sound("./sounds/RIM.wav")

    def play(self,count):
        if count == 1:
            self.channel.play(self.hat)
        else:
            self.channel.play(self.snare)

class Notes:
    '''
    This while be the random note generator
    should handle the playing of the audio.
    Also should return values in order for the met class to draw all the stuff
    '''
    pass 