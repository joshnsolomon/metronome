import pygame
from widgets import Button, Switch
from audio import Beats

class Met:

    #PyGame Stuff
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((1280,720))
    clock = pygame.time.Clock()
    big_font = pygame.font.SysFont('Comic Sans MS', 230)
    small_font = pygame.font.SysFont('Comic Sans MS', 100)

    #settings
    background = "purple"
    fps = 24
    max_tempo = 300
    
    #audio stuff
    beats = Beats()

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
                    self.restarting = True
                    self.count = 1

    def update(self):
        self.screen.fill(self.background) #draw background
        
        self.draw_button(self.up)
        self.draw_button(self.down)

        self.draw_play(self.play_button)

        self.draw_bpm([20, 600])

        self.click()

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

            #center the number
            X, Y = self.screen.get_size()
            x, y = self.big_font.size(str(self.count))
            xPos = (X-x)/2
            yPos = (Y-y)/2

            #draw
            text_surface = self.big_font.render(str(self.count), False, (0, 0, 0))
            self.screen.blit(text_surface, (xPos,yPos))
            

            
        else:
            #center the number
            X, Y = self.screen.get_size()
            x, y = self.big_font.size(str(self.count))
            xPos = (X-x)/2
            yPos = (Y-y)/2

            #draw
            text_surface = self.big_font.render(str(self.count), False, (0, 0, 0))
            self.screen.blit(text_surface, (xPos,yPos))


    def draw_button(self, button):
        self.screen.blit(button.surface,button.location)

    def draw_bpm(self, position):
        text_surface = self.small_font.render(str(self.bpm) + " BPM", False, (0, 0, 0))
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

    def flip(self):
        pygame.display.flip()

    def tick(self):
        self.clock.tick(self.fps)

    def quit(self):
        pygame.quit()


