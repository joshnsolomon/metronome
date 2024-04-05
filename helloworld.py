import pygame # type: ignore

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

print("font module is running:" + str(pygame.font.get_init()))

my_font = pygame.font.SysFont('Comic Sans MS', 230)

count = 0

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.time.delay(500)

    # metronome count
    count = (count)%4 + 1

    # centering the screen position
    X, Y = screen.get_size()
    x, y = my_font.size(str(count))
    xPos = X/2 - (x/2)
    yPos = Y/2 - (y/2)


    # RENDER YOUR GAME HERE
    #display text
    text_surface = my_font.render(str(count), False, (0, 0, 0))
    screen.blit(text_surface, (xPos,yPos))

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(24)  # limits FPS to 24

pygame.quit()
