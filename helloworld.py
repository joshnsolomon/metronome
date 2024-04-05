import pygame # type: ignore
from fyuncs import *

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

#print("font module is running:" + str(pygame.font.get_init()))
my_font = pygame.font.SysFont('Comic Sans MS', 230)
count = 1
bpm = 120
timer = 0

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    #pygame.time.delay(500)

    # RENDER YOUR GAME HERE
    timer += clock.get_time()
    if(timer >= (60000/bpm)):
        count = (count)%4 + 1
        print(timer)
        timer = 0

    click(my_font, screen, count)
    # print(clock.get_time())

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(24)  # limits FPS to 24

pygame.quit()
