import pygame
from widgets import Button, Switch
from audio import Beats, Notes

class Met:

    #PyGame Stuff
    pygame.init()
    screen = pygame.display.set_mode((1280,720))
    clock = pygame.time.Clock()
    small_font = pygame.font.Font('./font/Comic Sans MS.ttf', 66)
    medium_font = pygame.font.Font('./font/Comic Sans MS.ttf', 100)
    big_font = pygame.font.Font('./font/Comic Sans MS.ttf', 154)
    extra_big_font = pygame.font.Font('./font/Comic Sans MS.ttf', 250)

    #settings
    background = "purple"
    fps = 60
    max_tempo = 300
    
    #audio stuff
    beats = Beats()
    notes = Notes()

    #buttons that don't change
    up = Button('./images/up.png',[20,20])
    down = Button('./images/down.png',[20,300])

    def __init__(self):

        self.running = True

        #user stuff
        self.count = 1
        self.max_count = 4
        self.bpm = 120
        self.bpm_step = 10
        self.timer = 0
        self.restarting = True

        #buttons that do change - locations will be defined in the draw function
        self.play_button = Switch(["./images/play.png","./images/pause.png"], [0,0]) 


    def event_handle(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if self.up.is_inside(pos): #tempo up
                    self.bpm = min(self.bpm + self.bpm_step, self.max_tempo)
                if self.down.is_inside(pos): #tempo down
                    self.bpm = max(self.bpm - self.bpm_step, self.bpm_step)
                if self.play_button.is_inside(pos):
                    self.play_button.toggle()
                    self.notes.stop()
                    self.restarting = True
                    self.count = 1

    def update(self):
        self.screen.fill(self.background) #draw background
        
        self.draw_button(self.up)
        self.draw_button(self.down)

        self.draw_play(self.play_button)

        self.draw_bpm([20, 600])

        self.click()

        self.draw_notes(self.notes)

    def should_i_click(self):
        self.timer += self.clock.get_time()
        if self.timer >= (60000/self.bpm) and self.play_button.current_state:
            print (self.timer) #comment this out later
            self.timer = 0 
            return True
        else:
            return False    

    def click(self):
        if self.should_i_click():
            #this is so it plays the first beat after restarting
            if self.restarting:
                self.count = self.max_count
                self.restarting = False
            
            #increment beat
            self.count = self.count%self.max_count + 1 

            #play click sounds
            self.beats.play(self.count)
            self.notes.play(self.count)

            #center the number
            X, Y = self.screen.get_size()
            x, y = self.extra_big_font.size(str(self.count))
            xPos = (X-x)/2
            yPos = (Y-y)/2

            #draw
            text_surface = self.extra_big_font.render(str(self.count), False, (0, 0, 0))
            self.screen.blit(text_surface, (xPos,yPos))
            

            
        else:
            #center the number
            X, Y = self.screen.get_size()
            x, y = self.extra_big_font.size(str(self.count))
            xPos = (X-x)/2
            yPos = (Y-y)/2

            #draw
            text_surface = self.extra_big_font.render(str(self.count), False, (0, 0, 0))
            self.screen.blit(text_surface, (xPos,yPos))


    def draw_button(self, button):
        self.screen.blit(button.surface,button.location)

    def draw_bpm(self, position):
        text_surface = self.medium_font.render(str(self.bpm) + " BPM", False, (0, 0, 0))
        self.screen.blit(text_surface, position)

    def draw_play(self, switch):
        #draw in the middle at the top
        X, Y = self.screen.get_size()
        x = switch.surface.get_width()
        n, y = self.big_font.size(str(self.count))
        xPos = (X-x)/2
        yPos = Y/2 + y/2 

        switch.location = [xPos, yPos]
        self.screen.blit(switch.surface, switch.location)

    def draw_notes(self, notes):
        xpad = 20
        ypad = 0
        yshorten = 30
        X, Y = self.screen.get_size()
        
        #figure out the max width of the incoming notes set where the label will go
        max_width = 0
        max_height = 0
        for i in notes.key:
            wid, hyt = self.big_font.size(i)
            if wid > max_width:
                max_width = wid
            if hyt > max_height:
                max_height = hyt

        #draw current note
        current_surface = self.big_font.render(notes.current_note, False, (0, 0, 0))    
        x1 = current_surface.get_width()
        y1 = current_surface.get_height()
        xPos1 = X - x1 - xpad
        yPos1 = ypad - yshorten
        self.screen.blit(current_surface, (xPos1,yPos1))

        #draw label for current note
        current_label_surface = self.small_font.render("Current Note:", False, (0,0,0))
        x2 = current_label_surface.get_width()
        y2 = current_label_surface.get_height()
        xPos2 = X - xpad - max_width - x2
        yPos2 = yPos1  + (max_height- y2)/2
        self.screen.blit(current_label_surface, (xPos2,yPos2))

        #draw next note
        next_surface = self.big_font.render(notes.next_note, False, (0, 0, 0))
        x3 = next_surface.get_width()
        y3 = next_surface.get_height()
        xPos3 = X - xpad - x3
        yPos3 = ypad + max_height - 2*yshorten 
        self.screen.blit(next_surface, (xPos3, yPos3)) 
                
        #draw label for next note
        next_label_surface = self.small_font.render("Next Note:", False, (0,0,0))
        x4 = next_label_surface.get_width()
        y4 = next_label_surface.get_height()
        xPos4 = X - xpad - max_width - x4
        yPos4 = yPos1  + max_height + (max_height- y4)/2 - yshorten
        self.screen.blit(next_label_surface, (xPos4,yPos4))

    def flip(self):
        pygame.display.flip()

    def tick(self):
        self.clock.tick(self.fps)

    def quit(self):
        pygame.quit()


