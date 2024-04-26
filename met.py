import pygame
from widgets import Button, Switch
from audio import Beats, Notes
import os
base = os.path.dirname(__file__)


class Met:

    #PyGame Stuff
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((1280,720))
    icon = pygame.image.load(os.path.join(base,'./images/icon.png'))
    pygame.display.set_icon(icon)
    pygame.display.set_caption('Metronome')
    clock = pygame.time.Clock()
    small_font = pygame.font.Font(os.path.join(base,'./fonts/Comic Sans MS.ttf'), 66)
    medium_font = pygame.font.Font(os.path.join(base,'./fonts/Comic Sans MS.ttf'), 100)
    big_font = pygame.font.Font(os.path.join(base,'./fonts/Comic Sans MS.ttf'), 154)
    extra_big_font = pygame.font.Font(os.path.join(base,'./fonts/Comic Sans MS.ttf'), 250)

    #settings
    background = "purple"
    fps = 60
    max_tempo = 300
    
    #audio stuff
    beats = Beats()
    notes = Notes()

    #buttons that don't change
    up = Button(os.path.join(base,'./images/up.png'),[20,20])
    down = Button(os.path.join(base,'./images/down.png'),[20,300])

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
        self.play_button = Switch([os.path.join(base,"./images/play.png"),os.path.join(base,"./images/pause.png")], [0,0]) 
        self.note_switch = Switch([os.path.join(base,"./images/off.png"),os.path.join(base,"./images/on.png")], [0,0]) 
        self.time_sig = Switch([os.path.join(base,"images/4.png"), os.path.join(base,"images/3.png")])
    
    '''
    HANDLES ALL THE USER INPUT
    '''
    def event_handle(self):
        for event in pygame.event.get():
            #quit
            if event.type == pygame.QUIT:
                self.running = False

            #mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if self.up.is_inside(pos): #tempo up
                    self.tempo_up()
                if self.down.is_inside(pos): #tempo down
                    self.tempo_down()
                if self.time_sig.is_inside(pos):
                    self.change_time_sig()
                if self.play_button.is_inside(pos): #play pause
                    self.play_pause()
                if self.note_switch.is_inside(pos): #note generator
                    self.switch_note_gen()

            #keyboard
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: #play pause
                    self.play_pause()
                    self.notes.randomize()
                if event.key == pygame.K_UP: #tempo up
                    self.tempo_up()
                if event.key == pygame.K_DOWN: #tempo down
                    self.tempo_down()
                if event.key == pygame.K_n: #toggle note gen
                    self.switch_note_gen()
                if event.key == pygame.K_3: #change to 3/4
                    if self.time_sig.current_state == 0:
                        self.change_time_sig()
                if event.key == pygame.K_4: #change to 4/4
                    if self.time_sig.current_state == 1:
                        self.change_time_sig()


    '''            
    DRAWS THE WINDOW EVERY FRAME
    '''
    def update(self):
        self.screen.fill(self.background) #draw background
        
        self.draw_button(self.up)
        self.draw_button(self.down)

        self.draw_time_sig(self.time_sig)

        self.draw_play(self.play_button)

        self.draw_bpm([20, 600])

        self.click()

        self.draw_note_switch(self.note_switch)

        if self.note_switch.current_state:
            self.draw_notes(self.notes)

    '''
    ############################################################################
    CLICK METHODS
    These two methods are for the click, should I click is for figuring out 
    on which frames the metronome should click. And click handles all the 
    logic of the click itself. 
    ############################################################################
    '''
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
            if self.note_switch.current_state:
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

    '''
    ############################################################################
    DRAW METHODS
    these draw all the individual little things every frame.
    ############################################################################
    '''
    def draw_button(self, button):
        self.screen.blit(button.surface,button.location)

    def draw_bpm(self, position):
        text_surface = self.medium_font.render(str(self.bpm) + " BPM", False, (0, 0, 0))
        self.screen.blit(text_surface, position)

    def draw_time_sig(self, switch):
        x = self.up.surface.get_width()
        y = (280 + self.down.surface.get_height())/2 - switch.surface.get_height()/2 + 20
        switch.location = (x,y)
        self.screen.blit(switch.surface, switch.location)

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

    def draw_note_switch(self, switch):
        xpad = 10
        X, Y = self.screen.get_size()
        text = self.small_font.render('Note Generator', False, (0, 0, 0))
        x, y = text.get_size()
        xPos1 = X-x - xpad
        yPos1 = Y-y
        self.screen.blit(text, (xPos1, yPos1))

        x2, y2 = switch.surface.get_size()
        xPos2 = xPos1 - x2
        yPos2 = Y - y/2 - y2/2
        switch.location = (xPos2, yPos2)
        self.screen.blit(switch.surface, switch.location)
    
    '''
    ############################################################################
    USER INPUT
    All these function conatin the logic of what to do with user input
    ############################################################################
    '''
    def tempo_up(self):
        self.bpm = min(self.bpm + self.bpm_step, self.max_tempo)

    def tempo_down(self):
        self.bpm = max(self.bpm - self.bpm_step, self.bpm_step)

    def change_time_sig(self):
        self.time_sig.toggle()
        if self.time_sig.current_state == 0:
            self.max_count = 4
        if self.time_sig.current_state == 1:
            self.max_count = 3 
            if self.count == 4: #this is so that it doesn't play the hat twice
                self.count -= 1

    def play_pause(self):
        self.play_button.toggle()
        self.notes.stop()
        self.restarting = True
        self.count = 1
        self.notes.randomize()

    def switch_note_gen(self):
        self.note_switch.toggle()
        self.notes.channel.stop()
        self.notes.randomize()


    '''
    ############################################################################
    THIS STUFF
    I don't really know much about this stuff. But I call it in main.py
    .. so it must be important
    ############################################################################
    '''
    def flip(self):
        pygame.display.flip()

    def tick(self):
        self.clock.tick(self.fps)

    def quit(self):
        pygame.quit()


