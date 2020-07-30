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
while True:
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

    #print(ball_loc[1])
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

    pygame.display.update()
