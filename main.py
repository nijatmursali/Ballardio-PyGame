import pygame, sys

from pygame.locals import *
pygame.init() #initialize pygame

WINDOW_SIZE = (400, 400)

pygame.display.set_caption("Damn cool Game")
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)

right = False
left = False
up = False
ball_loc = [0, 300]

black_color = (0, 0, 0)
ball_image = pygame.image.load('images/ball_r.png')
ball_y_momentum = 0
angle = 0

isJump = False
jumpCount = 10

x = 20
y = 300
width = 40
height = 60
vel = 10

while True:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < WINDOW_SIZE[0] - width - vel:
        x += vel
    if not isJump:
        if keys[pygame.K_UP] and y > vel:
            y -= vel
        if keys[pygame.K_DOWN] and y < WINDOW_SIZE[1] - height - vel:
            y += vel
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    screen.fill(black_color)
    pygame.draw.rect(screen, (255,0,0), (x,y, width, height))
    pygame.display.update()

"""
    screen.fill(black_color)

    angle %= 360
    angle_ball = pygame.transform.rotate(ball_image, angle)

    screen.blit(angle_ball, ball_loc)
    if right == True:
        ball_loc[0] += 0.1
        angle -= 0.1
    if left == True:
        ball_loc[0] -= 0.1
        angle += 0.1

    if up == True:
        ball_y_momentum = 0.5
        ball_loc[1] -= ball_y_momentum
    else:
        ball_loc[1] += ball_y_momentum
        if ball_loc[1] >= 300:
            #print("baaaang!!!")
            ball_loc[1] = 300
        elif ball_loc[1] <= 0:
            print("puff")
            ball_loc[1] = 0
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                right = True
            if event.key == K_LEFT:
                left = True
            if event.key == K_UP:
                up = True
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                right = False
            if event.key == K_LEFT:
                left = False
            if event.key == K_UP:
                up = False
"""

