import pygame
import random
from pygame.examples.sprite_texture import running

pygame.init()
SCREEN_WIDTH=600
SCREEN_HEGHT=800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEGHT))
pygame.display.set_caption('Игра Тир')
icon = pygame.image.load('image/tir_icon.jpg')
pygame.display.set_icon(icon)
target_image = pygame.image.load('image/')
target_width = 50
target_height = 50
target_x = random.randint(0, SCREEN_WIDTH-target_width)
target_y = random.randint(0,SCREEN_HEGHT-target_height)
color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

runnig = True
while running:
    running = False

print('hi git')
pygame.quit()
