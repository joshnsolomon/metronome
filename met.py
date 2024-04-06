import pygame

class Met:

    background = "purple"
    fps = 24

    def __init__(self):

        #PyGame Stuff
        pygame.init()
        self.screen = pygame.display.set_mode((1280,720))
        self.clock = pygame.time.Clock()
        self.my_font = pygame.font.SysFont('Comic Sans MS', 230)
        self.running = True

        #user stuff
        self.count = 1
        self.max_count = 4
        self.bpm = 120
        self.timer = 0
        

    def event_handle(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def should_i_click(self):
        self.timer += self.clock.get_time()
        if(self.timer >= (60000/self.bpm)):
            print (self.timer)
            self.timer = 0 
            return True
        else:
            return False    

    def click(self):
        self.screen.fill(self.background) #draw background

        self.count = self.count%self.max_count + 1 #increment beat

        #center the number
        X, Y = self.screen.get_size()
        x, y = self.my_font.size(str(self.count))
        xPos = (X-x)/2
        yPos = (Y-y)/2

        #draw
        text_surface = self.my_font.render(str(self.count), False, (0, 0, 0))
        self.screen.blit(text_surface, (xPos,yPos))

    def flip(self):
        pygame.display.flip()

    def tick(self):
        self.clock.tick(self.fps)

    def quit():
        pygame.quit()


