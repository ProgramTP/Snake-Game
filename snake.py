import pygame
import random
import math

pygame.init()

width = 500
height = 500

main_window = pygame.display.set_mode((width,height))
pygame.display.set_caption("Snakaz")

x_pos = 100 #position of head of snake
y_pos = 100
x_change = 0
y_change = 0
snake_width = 10
snake_height = 10
ax = random.randrange(snake_width, width-snake_width, 10)
ay = random.randrange(snake_height, height-snake_height, 10)
apple = pygame.rect.Rect(ax, ay, 10, 10)
snakelist = []
snakeLen = 1
running = True
temp = True

def snake(snakelist):
    for x in snakelist:
        pygame.draw.rect(main_window, (255,255,255), [x[0],x[1],snake_width,snake_height])

def snakecollide(temp, snakelist, x_pos, y_pos):
    for x in snakelist:
        temp2 = pygame.draw.rect(main_window, (0,0,0), [x[0], x[1], 10, 10])
        if temp.colliderect(temp2):
            return True
    return False

while(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

    move = pygame.key.get_pressed()

    if move[pygame.K_UP]:
        x_change = 0
        y_change = -1
    if move[pygame.K_DOWN]:
        x_change = 0
        y_change = 1
    if move[pygame.K_LEFT]:
        y_change = 0
        x_change = -1
    if move[pygame.K_RIGHT]:
        y_change = 0
        x_change = 1

    x_pos += 10*x_change
    y_pos += 10*y_change

    if x_pos < 0 or x_pos > width - snake_width or y_pos < 0 or y_pos > height - snake_height:
        pygame.quit()

    if len(snakelist) > snakeLen:
        del snakelist[0]

    temp = pygame.draw.rect(main_window, (0,0,0), [x_pos,y_pos,10,10])
    if temp.colliderect(apple):
        ax = random.randrange(snake_width, width-snake_width, 10)
        ay = random.randrange(snake_height, height-snake_height, 10)
        snakeLen += 1

    if (snakeLen > 1):
        if snakecollide(temp, snakelist, x_pos, y_pos) == True:
            pygame.quit()

    main_window.fill((0,0,0))
    apple = pygame.draw.rect(main_window, (255,0,0), [ax,ay,10,10])
    snakeHead = []
    snakeHead.append(x_pos)
    snakeHead.append(y_pos)
    snakelist.append(snakeHead)
    snake(snakelist)
    pygame.display.update()
    pygame.time.delay(100)