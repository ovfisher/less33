from turtledemo.nim import SCREENWIDTH

import pygame
import random

pygame.init()
SCREEN_WIDTH=600
SCREEN_HEGHT=600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEGHT))
pygame.display.set_caption('Игра Тир')
icon = pygame.image.load('images/tir_icon.jpg')
pygame.display.set_icon(icon)
target_image = pygame.image.load('images/target.png')
target_width = 80
target_height = 80
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0,SCREEN_HEGHT - target_height)
color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

def sign() :
    k = random.randint(0,1)
    result = 2 * k - 1
    return result

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x+target_width and target_y < mouse_y < target_y+target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEGHT - target_height)

    screen.blit(target_image, (target_x,target_y))
# инкремент координат с проверкой и затем задержка на 800 мл сек
# получаем почти движение цели
#    target_y += target_y
#    target_x += target_x
#   target_y += random.randint(1, 20)
#   target_x += random.randint(1, 20)

    target_y = target_y + sign() * random.randint(1, 30)
    target_x = target_x + sign() * random.randint(1, 30)
    if target_y < target_height :
        target_y = SCREEN_HEGHT - target_height
    elif target_y > SCREEN_HEGHT - target_height :
        target_y = target_height

    if target_width > target_x :
        target_x = SCREEN_WIDTH - target_width
    elif target_x > SCREEN_WIDTH - target_width:
        target_x = target_width

#    pygame.time.delay(800)
    pygame.display.update()
    pygame.time.delay(100)

pygame.quit()
