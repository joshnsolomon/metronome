import pygame # type: ignore
from fyuncs import *

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
my_font = pygame.font.SysFont('Comic Sans MS', 230)
running = True

#constant values
count = 1
bpm = 120
timer = 0

for i in pygame.mixer.get_init():
    print(i)

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
        click(my_font, screen, count)
        
        if count == 1:
            continue
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(24)  # limits FPS to 24

pygame.quit()
