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
sphere_x = 110
sphere_y = 10
speed = 5
radius = 110
points = ((250, 200), (400, 50), (550, 200))
circlecolor = ((255, 255, 0))
bgcolor = ((80, 131, 197))
# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # GAME STATE UPDATES
    # All game math and comparisons happen here

    sphere_y += speed
    if sphere_y > HEIGHT + radius:
        circlecolor = ((64, 64, 64))
        bgcolor = ((0, 0, 0))
        speed *= -1
    if sphere_y < 0 - radius:
        circlecolor = ((255, 255, 0))
        bgcolor = ((80, 131, 197))
        speed *= -1
    
        

    # DRAWING
    screen.fill(bgcolor)  # always the first drawing command

    pygame.draw.rect(screen, (198, 188, 164), (face_x+200, face_y+200, face_x+100, face_y+200))
    pygame.draw.rect(screen, (198, 188, 164), (face_x+350, face_y + 50, face_x-50, face_y+100))
    pygame.draw.polygon(screen, (168, 45, 42), ((face_x+150, face_y+199), (face_x+300, face_y+49), (face_x+450, face_y+199)))
    pygame.draw.circle(screen, circlecolor, (face_x+10, sphere_y), face_x-80)  # sun
    pygame.draw.rect(screen, (30, 97, 66), (face_x-100, face_y+400, face_x+2000, face_y+200))  #ground
    for x in range(50, 101, 25):
        pygame.draw.rect(screen, (198, 188, 164), (face_x+200, face_y+199, face_x+100, face_y+200))
    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()
