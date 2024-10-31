import pygame


pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables
face_x = 100
face_y = 1
speed = 5
radius = 110
sun_x = 100
sun_y = 100
points = ((250, 200), (400, 50), (550, 200))
suncolor = ((224, 217, 0))
suncolor2 = ((191, 185, 2))
suncolor3 = ((224, 217, 0))
bgcolor = ((80, 131, 197))
# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)

    # GAME STATE UPDATES
    # All game math and comparisons happen here

    sun_y += speed

    if sun_y > HEIGHT + radius and sun_y > HEIGHT + radius:
        suncolor = ((64, 64, 64))
        suncolor2 = ((77, 77, 77))
        suncolor3 = ((0,0,0))
        bgcolor = ((0, 0, 0))
        speed *= -1

    if sun_y < 0 - radius and sun_y < 0 - radius:
        suncolor = ((184, 156, 17))
        suncolor2 = ((191, 185, 2))
        suncolor3 = ((224, 217, 0))
        bgcolor = ((80, 131, 197))
        speed *= -1

    
    
        

    # DRAWING
    screen.fill(bgcolor)  # always the first drawing command

    pygame.draw.rect(screen, (198, 188, 164), (face_x+200, face_y+200, face_x+100, face_y+200))
    pygame.draw.rect(screen, (198, 188, 164), (face_x+350, face_y + 50, face_x-50, face_y+100))
    pygame.draw.polygon(screen, (168, 45, 42), ((face_x+150, face_y+199), (face_x+300, face_y+49), (face_x+450, face_y+199)))
    pygame.draw.line(screen, suncolor3, (80, sun_y+27), (135, sun_y-31), 7)
    pygame.draw.line(screen, suncolor3, (134, sun_y+27), (85, sun_y-31), 7)
    pygame.draw.rect(screen, (suncolor3), (sun_x-28, sun_y-2, 75, 5))
    pygame.draw.rect(screen, (suncolor3), (sun_x+7.75, sun_y-35, 5, 75))
    pygame.draw.circle(screen, (suncolor), (sun_x+10, sun_y), 20)
    pygame.draw.circle(screen, (suncolor2), (sun_x+10, sun_y), 15)  # sun

    pygame.draw.rect(screen, (1, 102, 31), (face_x-100, face_y+400, face_x+2000, face_y+200))  #ground
    for x in range(50, 101, 25):
        pygame.draw.rect(screen, (198, 188, 164), (face_x+200, face_y+199, face_x+100, face_y+200))
    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()
