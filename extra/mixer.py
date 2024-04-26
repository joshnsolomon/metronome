import pygame # type: ignore

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
my_font = pygame.font.SysFont('Comic Sans MS', 230)
running = True

#constant values
count = 0
bpm = 120
timer = 0

#sounds 
hat = pygame.mixer.Sound("./sounds/HAT.wav")
cnote = pygame.mixer.Sound("./sounds/C.wav")

beats = pygame.mixer.Channel(1)
notes = pygame.mixer.Channel(2)



print(pygame.mixer.get_num_channels())

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # RENDER YOUR GAME HERE
    timer += clock.get_time()
    if timer >= 60000/bpm:
        count = (count)%4 + 1
        print(timer)
        timer = 0

        screen.fill("purple")
        X, Y = screen.get_size()
        x, y = my_font.size(str(count))
        xPos = X/2 - (x/2)
        yPos = Y/2 - (y/2)
        
        text_surface = my_font.render(str(count), False, (0, 0, 0))
        screen.blit(text_surface, (xPos,yPos))

        beats.play(hat) 
        
        if count == 1:
            notes.play(cnote)
        if count == (3 or 4):
            notes.stop()
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(24)  # limits FPS to 24

pygame.quit()
