import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT

pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)
circle_x = 10
circle_y = 10
circle_r = 30

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    # GAME STATE UPDATES
    # All game math and comparisons happen here
    circle_x += 10
    if circle_x > WIDTH + circle_r:
     circle_x = -circle_r

    # DRAWING
    screen.fill((255, 255, 255))  # always the first drawing command
    pygame.draw.circle(screen, (0, 0, 255), (circle_x, circle_y), circle_r)

    # Move on y axis
    # Wrap around y axis
    # Red ball moving
    # Rebound red ball off screen
    
    # red circle
    pygame.draw.rect(screen, (255, 255, 0), (0, 0, 50, 50))
    pygame.draw.circle(screen, (255, 0, 0), (100, 100), 50)
    # rectangle
    pygame.draw.rect(screen, (200, 0, 0), (0, 0, 50, 75))

    # circle
    pygame.draw.circle(screen, (0, 200, 0), (100, 300), 20)

    # ellipse
    pygame.draw.ellipse(screen, (255, 255, 255), (100, 0, 50, 75))

    # line

    # arc


    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()