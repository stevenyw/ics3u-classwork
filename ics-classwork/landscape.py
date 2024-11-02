import pygame


pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
# ---------------------------
# Initialize global variables
pos_x = 100
pos_y = 1
speed = 5
radius = 110
sun_x = 100
sun_y = 100
points = ((250, 200), (400, 50), (550, 200))
suncolor = ((224, 217, 0))
suncolor2 = ((191, 185, 2))
suncolor3 = ((224, 217, 0))
bgcolor = ((80, 131, 197))
nightsky = 1
star_color = ((80, 131, 197))
roof_color = ((168, 45, 42))
house_color = ((198, 188, 164))
streetlight = ((92, 92, 92))
brightlight = ((125, 124, 124))
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
    
    if sun_y > HEIGHT + radius:
        suncolor = ((64, 64, 64))
        suncolor2 = ((77, 77, 77))
        suncolor3 = ((0,0,0))
        bgcolor = ((0,0,0))
        star_color = ((255,255,255))
        roof_color = ((102, 27, 26))
        house_color = ((168, 160, 141))
        streetlight = ((33, 33, 33))
        brightlight = ((224, 221, 2))
        speed *= -1

    elif sun_y < 0 - radius:
        suncolor = ((184, 156, 17))
        suncolor2 = ((191, 185, 2))
        suncolor3 = ((224, 217, 0))
        bgcolor = ((80, 131, 197))
        star_color = ((80, 131, 197))
        roof_color = ((168, 45, 42))
        house_color = ((198, 188, 164))
        streetlight = ((92, 92, 92))
        brightlight = ((125, 124, 124))
        speed *= -1

    # DRAWING
    screen.fill(bgcolor)  # always the first drawing command
# House!!!!!!!!!!!!!!
    pygame.draw.rect(screen, (house_color), (pos_x+200, pos_y+200, 200, 201))
    pygame.draw.rect(screen, (house_color), (pos_x+350, pos_y + 50, 50, 101))
    pygame.draw.polygon(screen, (roof_color), ((pos_x+150, pos_y+199), (pos_x+300, pos_y+49), (pos_x+450, pos_y+199)))

# starry -w-

    pygame.draw.line(screen, (star_color), (200, 30), (230, 30), 2)
    pygame.draw.line(screen, (star_color), (215, 17), (215, 44), 2)
    pygame.draw.line(screen, (star_color), (223, 22), (207, 42), 2)
    pygame.draw.line(screen, (star_color), (207, 22), (223, 42), 2)

    pygame.draw.line(screen, (star_color), (320, 80), (350, 80), 2)
    pygame.draw.line(screen, (star_color), (335, 67), (335, 94), 2)
    pygame.draw.line(screen, (star_color), (343, 72), (327, 92), 2)
    pygame.draw.line(screen, (star_color), (327, 72), (343, 92), 2)

    pygame.draw.line(screen, (star_color), (540, 90), (570, 90), 2)
    pygame.draw.line(screen, (star_color), (555, 77), (555, 104), 2)
    pygame.draw.line(screen, (star_color), (563, 82), (547, 102), 2)
    pygame.draw.line(screen, (star_color), (547, 82), (563, 102), 2)

    pygame.draw.line(screen, (star_color), (450, 20), (480, 20), 2)
    pygame.draw.line(screen, (star_color), (465, 7), (465, 34), 2)
    pygame.draw.line(screen, (star_color), (473, 12), (457, 32), 2)
    pygame.draw.line(screen, (star_color), (457, 12), (473, 32), 2)

    pygame.draw.line(screen, (star_color), (200, 30), (230, 30), 2)
    pygame.draw.line(screen, (star_color), (215, 17), (215, 44), 2)
    pygame.draw.line(screen, (star_color), (223, 22), (207, 42), 2)
    pygame.draw.line(screen, (star_color), (207, 22), (223, 42), 2)

    pygame.draw.line(screen, (star_color), (320, 80), (350, 80), 2)
    pygame.draw.line(screen, (star_color), (335, 67), (335, 94), 2)
    pygame.draw.line(screen, (star_color), (343, 72), (327, 92), 2)
    pygame.draw.line(screen, (star_color), (327, 72), (343, 92), 2)

    pygame.draw.line(screen, (star_color), (540, 90), (570, 90), 2)
    pygame.draw.line(screen, (star_color), (555, 77), (555, 104), 2)
    pygame.draw.line(screen, (star_color), (563, 82), (547, 102), 2)
    pygame.draw.line(screen, (star_color), (547, 82), (563, 102), 2)

    pygame.draw.line(screen, (star_color), (450, 20), (480, 20), 2)
    pygame.draw.line(screen, (star_color), (465, 7), (465, 34), 2)
    pygame.draw.line(screen, (star_color), (473, 12), (457, 32), 2)
    pygame.draw.line(screen, (star_color), (457, 12), (473, 32), 2)

    pygame.draw.line(screen, (star_color), (580, 50), (610, 50), 2)
    pygame.draw.line(screen, (star_color), (595, 37), (595, 64), 2)
    pygame.draw.line(screen, (star_color), (603, 42), (587, 62), 2)
    pygame.draw.line(screen, (star_color), (587, 42), (603, 62), 2)

    pygame.draw.line(screen, (star_color), (150, 100), (180, 100), 2)
    pygame.draw.line(screen, (star_color), (165, 87), (165, 114), 2)
    pygame.draw.line(screen, (star_color), (173, 92), (157, 112), 2)
    pygame.draw.line(screen, (star_color), (157, 92), (173, 112), 2)


    # sun
    pygame.draw.line(screen, suncolor3, (80, sun_y+27), (135, sun_y-31), 7)
    pygame.draw.line(screen, suncolor3, (134, sun_y+27), (85, sun_y-31), 7)
    pygame.draw.rect(screen, (suncolor3), (sun_x-28, sun_y-2, 75, 5))
    pygame.draw.rect(screen, (suncolor3), (sun_x+7.75, sun_y-35, 5, 75))
    pygame.draw.circle(screen, (suncolor), (sun_x+10, sun_y), 20)
    pygame.draw.circle(screen, (suncolor2), (sun_x+10, sun_y), 15)

    # ground
    pygame.draw.rect(screen, (1, 102, 31), (pos_x-100, pos_y+400, 2100, 201))
    pygame.draw.rect(screen, (122, 98, 61), (pos_x+265, pos_y+330, 60, 70))  #ground
    for x in range(50, 101):
        pygame.draw.rect(screen, (house_color), (pos_x+200, pos_y+199, 200, 201))
        pygame.draw.rect(screen, (175, 141, 89), (pos_x+255, pos_y+330, 10, 70))
        pygame.draw.rect(screen, (175, 141, 89), (pos_x+325, pos_y+330, 10, 70))
        pygame.draw.rect(screen, (175, 141, 89), (pos_x+265, pos_y+320, 60, 10))
        pygame.draw.rect(screen, (122, 98, 61), (pos_x+265, pos_y+330, 60, 70))
        
    pygame.draw.rect(screen, (streetlight), (pos_x+75, pos_y+250, 25, 150))
    pygame.draw.rect(screen, (brightlight), (pos_x+56, pos_y+200, 65, 65))
        
    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()
