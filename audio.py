import pygame
import random
import os
base = os.path.dirname(__file__)

class Beats:
    # might have to change this to pygame.mixer.find_channel()
    
    def __init__(self):

        self.channel = pygame.mixer.Channel(1)
        self.channel.set_volume(0.3)

        self.hat =   pygame.mixer.Sound(os.path.join(base,"./sounds/HAT.wav"))
        self.snare = pygame.mixer.Sound(os.path.join(base,"./sounds/SNARE.wav"))
        self.rim =   pygame.mixer.Sound(os.path.join(base,"./sounds/RIM.wav"))
        self.kick =   pygame.mixer.Sound(os.path.join(base,"./sounds/KICK.wav"))
        

    def play(self,count):
        if count == 1:
            self.channel.play(self.kick)
        if count == 2 or count == 4:
            self.channel.play(self.hat)
        if count == 3:
            self.channel.play(self.snare)

class Notes:
    '''
    This while be the random note generator
    should handle the playing of the audio.
    Also should return values in order for the met class to draw all the stuff
    '''
    def __init__(self):
        self.channel = pygame.mixer.Channel(2)

        self.C   = pygame.mixer.Sound(os.path.join(base,"./sounds/C.wav"))
        self.Csh = pygame.mixer.Sound(os.path.join(base,"./sounds/C#.wav")) 
        self.D   = pygame.mixer.Sound(os.path.join(base,"./sounds/D.wav") ) 
        self.Dsh = pygame.mixer.Sound(os.path.join(base,"./sounds/D#.wav")) 
        self.E   = pygame.mixer.Sound(os.path.join(base,"./sounds/E.wav") ) 
        self.F   = pygame.mixer.Sound(os.path.join(base,"./sounds/F.wav") ) 
        self.Fsh = pygame.mixer.Sound(os.path.join(base,"./sounds/F#.wav"))
        self.G   = pygame.mixer.Sound(os.path.join(base,"./sounds/G.wav") ) 
        self.Gsh = pygame.mixer.Sound(os.path.join(base,"./sounds/G#.wav")) 
        self.A   = pygame.mixer.Sound(os.path.join(base,"./sounds/A.wav") )
        self.Ash = pygame.mixer.Sound(os.path.join(base,"./sounds/A#.wav"))
        self.B   = pygame.mixer.Sound(os.path.join(base,"./sounds/B.wav") )

        self.key = {'C':self.C, 'D':self.D, 'E':self.E,
                    'F':self.F, 'G':self.G, 'A':self.A, 'B':self.B}
        self.current_note = ' '
        self.next_note = ' '


    def play(self,count):
        if count == 1:
            #make next note the current note and play it and
            self.current_note = self.next_note
            if self.current_note in self.key.keys():
                self.channel.play(self.key[self.current_note])

            #pick a random different next note
            self.next_note = random.choice([x for x in self.key.keys() if x != self.next_note])
        if count == 4:
            pass #self.channel.stop()
    
    def stop(self):
        self.channel.stop()

    def randomize(self):
        self.current_note = '^'
        self.next_note = '^' 