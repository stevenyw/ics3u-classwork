import pygame


pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables

circle_x = 200
circle_y = 200
circle_x_speed = 10
circle_y_speed = 5
radius = 30

# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # GAME STATE UPDATES
    # All game math and comparisons happen here

    if circle_x + radius > WIDTH or circle_x - radius < 0:
        circle_x_speed *= -1

    if circle_y + radius > HEIGHT or circle_y - radius < 0:
        circle_y_speed *= -1

    circle_x += circle_x_speed
    circle_y += circle_y_speed
    # DRAWING
    screen.fill((255, 255, 255))  # always the first drawing command

    pygame.draw.circle(screen, (0, 0, 255), (circle_x, circle_y), 30)

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()
